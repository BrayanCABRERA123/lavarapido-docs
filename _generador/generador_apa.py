"""Builds APA 7 formatted PDFs from the manual Markdown files.

Markdown subset supported (the one used by the manuals):
  - <!-- running-head: TEXT --> comment for the running head.
  - Title page: everything before the first "## " heading.
  - "## Table of Contents" followed by <!-- toc --> ... <!-- /toc -->: regenerated in the MD
    and rendered with real page numbers in the PDF (two-pass rendering).
  - Headings ## (APA level 1), ### (level 2), #### (level 3), ##### (level 4, run-in).
  - Paragraphs, "- " bullet lists, "1. " numbered lists, pipe tables, ``` code fences,
    "> " blockquotes (screenshot placeholders), ![alt](file.svg) figures.
  - "**Table N**" / "**Figure N**" + "*Title*" captions and "*Note.*" notes.
  - "## References": hanging-indent reference list on a new page.
  - Spanish documents are detected by their "**Tabla N**" / "**Figura N**" captions; they
    also accept "*Nota.*", "## Control de Versiones", "## Tabla de Contenido",
    "## Referencias" and "Anexo" headings, and keep their headings as written.
Usage: python generador_apa.py <md>=<pdf> [...] (normalmente lo llama generar.py)
"""
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PDFTOTEXT = r"C:\Program Files\Git\mingw64\bin\pdftotext.exe"

MINOR_WORDS = {"a", "an", "the", "and", "but", "or", "nor", "for", "so", "yet", "as", "at",
               "by", "in", "of", "off", "on", "per", "to", "up", "via", "vs", "vs.", "with"}
# APA title case: words of four letters or more are capitalized, "with" is the only
# common 4-letter word kept lowercase by many guides, but APA capitalizes it.
MINOR_WORDS.discard("with")

NEW_PAGE_HEADINGS = {"version control", "table of contents", "references",
                     "control de versiones", "tabla de contenido", "referencias"}
TOC_HEADINGS = ("table of contents", "tabla de contenido")
REF_HEADINGS = ("references", "referencias")
ANNEX_PREFIXES = ("annex", "anexo")
LANG = {"value": "en"}
BASE_DIR = {"value": "."}


def title_case(text):
    """APA 7 title case that leaves identifiers (code, paths, acronyms) untouched.
    Spanish documents are already written with their final capitalization."""
    if LANG["value"] == "es":
        return text
    words = text.split(" ")
    out = []
    capitalize_next = True
    for i, w in enumerate(words):
        core = w.strip("()[]\"'“”‘’,;:")
        is_identifier = (
            not core
            or any(c in core for c in "._/@<>=`\\")
            or any(c.isdigit() for c in core)
            or (core.upper() == core and any(c.isalpha() for c in core))
            or any(c.isupper() for c in core[1:])
            or core.endswith("-service") or core in ("api-gateway", "lavarapido-infra")
        )
        if is_identifier:
            out.append(w)
        else:
            lower = w.lower()
            if not capitalize_next and core.lower() in MINOR_WORDS and i != len(words) - 1:
                out.append(lower)
            else:
                parts = lower.split("-")
                parts = [p[:1].upper() + p[1:] if p and (j == 0 or len(p) > 3) else p
                         for j, p in enumerate(parts)]
                fixed = "-".join(parts)
                # keep leading punctuation such as "(" before capitalizing
                m = re.match(r"^([(\[\"'“‘]*)(.*)$", fixed)
                fixed = m.group(1) + m.group(2)[:1].upper() + m.group(2)[1:]
                out.append(fixed)
        capitalize_next = (w.endswith(":") or w.endswith("—")
                           or (i == 0 and is_identifier and core[:1].isdigit())
                           or (i <= 1 and words[0].lower() == "annex"))
    return " ".join(out)


def inline(text):
    """Inline Markdown: code, bold, italic, links."""
    text = re.sub(r"\*(`[^`]+`)\*", r"\1", text)
    parts = re.split(r"(`[^`]+`)", text)
    res = []
    for p in parts:
        if p.startswith("`") and p.endswith("`") and len(p) > 1:
            res.append("<code>" + html.escape(p[1:-1]) + "</code>")
            continue
        s = html.escape(p, quote=False)
        s = s.replace("\\*", "&#42;")
        s = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", lambda m: '<img class="inline-img" src="%s" alt="%s">' % (
            __import__("pathlib").Path(os.path.join(BASE_DIR["value"], m.group(2))).resolve().as_uri(), m.group(1)), s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
        s = re.sub(r"\b(\d{4}-\d{2}-\d{2})\b", r'<span class="nw">\1</span>', s)
        res.append(s)
    return "".join(res)


def slug(text):
    s = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s]+", "-", s).strip("-")


def read_blocks(lines):
    """Splits Markdown lines into typed blocks."""
    blocks = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        if stripped.startswith("<!--"):
            while i < n and "-->" not in lines[i]:
                i += 1
            blocks.append(("comment", lines[i].strip() if i < n else ""))
            i += 1
            continue
        if stripped.startswith("```"):
            i += 1
            code = []
            while i < n and not lines[i].strip().startswith("```"):
                code.append(lines[i].rstrip("\n"))
                i += 1
            i += 1
            blocks.append(("code", "\n".join(code)))
            continue
        m = re.match(r"^(#{1,5})\s+(.*)$", stripped)
        if m:
            blocks.append(("h%d" % len(m.group(1)), m.group(2).strip()))
            i += 1
            continue
        if stripped.startswith("|"):
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            blocks.append(("table", rows))
            continue
        if stripped.startswith(">"):
            quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            blocks.append(("quote", quote))
            continue
        if re.match(r"^(- |\d+\. )", stripped):
            ordered = bool(re.match(r"^\d+\. ", stripped))
            items = []
            while i < n and lines[i].strip() and (re.match(r"^(- |\d+\. )", lines[i].strip())
                                                  or lines[i].startswith("   ")):
                s = lines[i].strip()
                if re.match(r"^(- |\d+\. )", s):
                    items.append(re.sub(r"^(- |\d+\. )", "", s))
                else:
                    items[-1] += " " + s
                i += 1
            blocks.append(("ol" if ordered else "ul", items))
            continue
        para = []
        while i < n and lines[i].strip() and not re.match(r"^(#{1,5}\s|\||>|```|- |\d+\. )",
                                                          lines[i].strip()):
            para.append(lines[i].strip())
            i += 1
        blocks.append(("p", " ".join(para)))
    return blocks


def render_image(val, base_dir):
    m_img = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", val)
    path = os.path.join(base_dir, m_img.group(2))
    if path.lower().endswith(".svg") and os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            svg = f.read()
        svg = re.sub(r"<\?xml[^>]*\?>", "", svg)
        return '<div class="figure-img">%s</div>' % svg
    return '<div class="figure-img"><img src="%s" alt="%s"></div>' % (
        html.escape(__import__("pathlib").Path(path).resolve().as_uri()), html.escape(m_img.group(1)))


def render_table(rows, caption=""):
    def cells(r):
        r = r.strip().strip("|")
        return [c.strip() for c in re.split(r"(?<!\\)\|", r)]
    header = cells(rows[0])
    body = [cells(r) for r in rows[2:]]
    out = ['<table class="apa%s">' % (' small' if len(body) <= 14 else '') + ('<caption>%s</caption>' % caption if caption else '') + '<thead><tr>']
    out += ["<th>%s</th>" % inline(c) for c in header]
    out.append("</tr></thead><tbody>")
    for r in body:
        out.append("<tr>" + "".join("<td>%s</td>" % inline(c) for c in r) + "</tr>")
    out.append("</tbody></table>")
    return "".join(out)


def build_html(md_path, toc_pages=None, markers=True):
    with open(md_path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    blocks = read_blocks(lines)
    LANG["value"] = "es" if any(k == "p" and re.match(r"^\*\*(Tabla|Figura) \d+\*\*$", v)
                                for k, v in blocks) else "en"
    note_label = "Nota." if LANG["value"] == "es" else "Note."
    base_dir = os.path.dirname(os.path.abspath(md_path))
    BASE_DIR["value"] = base_dir

    running_head = ""
    for kind, val in blocks:
        if kind == "comment" and "running-head:" in val:
            running_head = val.split("running-head:")[1].replace("-->", "").strip()

    headings = []  # (level, text, id)
    for kind, val in blocks:
        if kind in ("h2", "h3"):
            headings.append((kind, val, "h-%d" % len(headings)))

    body = []
    title_page = []
    in_title = True
    in_toc = False
    in_refs = False
    pending_runin = None
    hidx = 0
    caption_open = None
    i = 0
    while i < len(blocks):
        kind, val = blocks[i]
        if in_title:
            if kind == "h2":
                in_title = False
                body.append('<section class="title-page">%s</section>' % "".join(title_page))
            else:
                if kind == "h1":
                    title_page.append('<h1 class="doc-title">%s</h1>' % inline(val))
                elif kind == "p" and val.strip() not in ("---", "***"):
                    title_page.append('<p class="tp">%s</p>' % inline(val))
                elif kind == "table":
                    title_page.append(render_table(val))
                i += 1
                continue
        if kind == "comment":
            if "<!-- toc -->" in val:
                in_toc = True
            elif "<!-- /toc -->" in val:
                in_toc = False
            i += 1
            continue
        if in_toc:
            i += 1
            continue
        if kind in ("h2", "h3", "h4", "h5"):
            caption_open = None
            text = val
            hid = None
            if kind in ("h2", "h3"):
                hid = headings[hidx][2]
                hidx += 1
            marker = ('<span class="mk">QQ%sQQ</span>' % hid.replace("-", "")) if (hid and markers) else ""
            low = text.lower()
            if kind == "h2":
                in_refs = low in REF_HEADINGS
                classes = "l1"
                if low in NEW_PAGE_HEADINGS or low.startswith("4. ") or low.startswith(ANNEX_PREFIXES):
                    classes += " newpage"
                body.append('<h2 id="%s" class="%s">%s%s</h2>' % (hid, classes, marker,
                                                                 inline(title_case(text))))
                if low in TOC_HEADINGS:
                    body.append(render_toc(headings, toc_pages))
            elif kind == "h3":
                cls = "l2 newpage" if low.startswith(ANNEX_PREFIXES) else "l2"
                body.append('<h3 id="%s" class="%s">%s%s</h3>' % (hid, cls, marker,
                                                                 inline(title_case(text))))
            elif kind == "h4":
                body.append('<h4 class="l3">%s</h4>' % inline(title_case(text)))
            else:
                t = title_case(text)
                if not t.endswith((".", "?", "!")):
                    t += "."
                pending_runin = '<span class="l4">%s</span> ' % inline(t)
            i += 1
            continue
        if kind == "p" and val.strip() in ("---", "***"):
            i += 1
            continue
        if kind == "p":
            m_cap = re.match(r"^\*\*(Table|Figure|Tabla|Figura) (\d+)\*\*$", val)
            if m_cap and i + 1 < len(blocks) and blocks[i + 1][0] == "p":
                title = blocks[i + 1][1].strip("*")
                cap = ('<p class="cap-num"><strong>%s %s</strong></p><p class="cap-title"><em>%s</em></p>'
                       % (m_cap.group(1), m_cap.group(2), inline(title_case(title))))
                nxt = blocks[i + 2] if i + 2 < len(blocks) else (None, None)
                if m_cap.group(1) in ("Table", "Tabla") and nxt[0] == "table":
                    body.append(render_table(nxt[1], cap))
                    i += 3
                    continue
                # figure: keep number, title and image/placeholder together on one page
                fig = ['<div class="figure-block"><div class="caption">%s</div>' % cap]
                if nxt[0] == "quote":
                    fig.append('<div class="placeholder">%s</div>'
                               % "".join("<p>%s</p>" % inline(q) for q in nxt[1] if q))
                    i += 3
                elif nxt[0] == "p" and re.match(r"^!\[", nxt[1] or ""):
                    fig.append(render_image(nxt[1], base_dir))
                    i += 3
                else:
                    i += 2
                if i < len(blocks) and blocks[i][0] == "p" and blocks[i][1].startswith(("*Note.*", "*Nota.*")):
                    fig.append('<p class="note"><em>%s</em>%s</p>' % (note_label, inline(blocks[i][1][len("*Note.*"):])))
                    i += 1
                fig.append("</div>")
                body.append("".join(fig))
                continue
            if val.startswith(("*Note.*", "*Nota.*")):
                body.append('<p class="note"><em>%s</em>%s</p>' % (note_label, inline(val[len("*Note.*"):])))
                caption_open = None
                i += 1
                continue
            if re.match(r"^!\[", val):
                body.append(render_image(val, base_dir))
                i += 1
                continue
            cls = "ref" if in_refs else ""
            content = inline(val)
            if pending_runin:
                content = pending_runin + content
                pending_runin = None
                cls = (cls + " runin").strip()
            body.append('<p class="%s">%s</p>' % (cls, content))
            i += 1
            continue
        if kind == "table":
            body.append(render_table(val))
            i += 1
            continue
        if kind == "code":
            body.append("<pre><code>%s</code></pre>" % html.escape(val))
            i += 1
            continue
        if kind == "quote":
            inner = "".join("<p>%s</p>" % inline(q) for q in val if q)
            cls = "placeholder" if caption_open == "Figure" else "callout"
            body.append('<div class="%s">%s</div>' % (cls, inner))
            i += 1
            continue
        if kind in ("ul", "ol"):
            items = "".join("<li>%s</li>" % inline(it) for it in val)
            body.append("<%s>%s</%s>" % (kind, items, kind))
            i += 1
            continue
        i += 1

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "apa.css"), encoding="utf-8") as f:
        css = f.read()
    css = css.replace("__RUNNING_HEAD__", running_head.replace('"', '\\"'))
    title = ""
    for kind, val in blocks:
        if kind == "h1":
            title = val
            break
    doc = ('<!doctype html><html lang="__LANG__"><head><meta charset="utf-8"><title>%s</title>'
           '<style>%s</style></head><body>%s</body></html>'
           % (html.escape(title), css, "\n".join(body)))
    doc = doc.replace("__LANG__", LANG["value"], 1)
    return doc, headings


def render_toc(headings, toc_pages):
    rows = ['<div class="toc">']
    for kind, text, hid in headings:
        if text.lower() in TOC_HEADINGS:
            continue
        page = "000"
        if toc_pages and hid in toc_pages:
            page = str(toc_pages[hid])
        cls = "toc1" if kind == "h2" else "toc2"
        rows.append('<div class="%s"><span class="tt">%s</span><span class="dots"></span>'
                    '<span class="pg">%s</span></div>' % (cls, inline(title_case(text)), page))
    rows.append("</div>")
    return "".join(rows)


def print_pdf(html_path, pdf_path, profile_dir):
    url = "file:///" + os.path.abspath(html_path).replace("\\", "/")
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
           "--generate-pdf-document-outline", "--user-data-dir=" + profile_dir,
           "--print-to-pdf=" + pdf_path, url]
    subprocess.run(cmd, check=True, capture_output=True)


def pdf_pages_text(pdf):
    out = subprocess.run([PDFTOTEXT, "-enc", "UTF-8", pdf, "-"], capture_output=True).stdout
    pages = out.decode("utf-8", errors="replace").split("")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    return pages


def page_count(pdf):
    return len(pdf_pages_text(pdf))


def find_marker_pages(pdf, headings):
    pages = {}
    for p, txt in enumerate(pdf_pages_text(pdf), start=1):
        for _, _, hid in headings:
            key = "QQ%sQQ" % hid.replace("-", "")
            if hid not in pages and key in txt:
                pages[hid] = p
    return pages


def update_md_toc(md_path):
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    lines = text.splitlines()
    heads = []
    fence = False
    for ln in lines:
        if ln.strip().startswith("```"):
            fence = not fence
        if fence:
            continue
        m = re.match(r"^(##|###)\s+(.*)$", ln)
        if m and m.group(2).strip().lower() not in TOC_HEADINGS:
            heads.append((len(m.group(1)), m.group(2).strip()))
    toc = ["<!-- toc -->", ""]
    for lvl, t in heads:
        indent = "" if lvl == 2 else "  "
        toc.append("%s- [%s](#%s)" % (indent, t, slug(t)))
    toc += ["", "<!-- /toc -->"]
    new = re.sub(r"<!-- toc -->.*?<!-- /toc -->", "\n".join(toc), text, flags=re.S)
    if new != text:
        with open(md_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(new)


def build(md_path, out_pdf, work):
    update_md_toc(md_path)
    profile = os.path.join(work, "chrome-profile")
    name = os.path.splitext(os.path.basename(out_pdf))[0]
    html1 = os.path.join(work, name + ".pass1.html")
    pdf1 = os.path.join(work, name + ".pass1.pdf")
    doc, headings = build_html(md_path, None, markers=True)
    with open(html1, "w", encoding="utf-8") as f:
        f.write(doc)
    print_pdf(html1, pdf1, profile)
    pages = find_marker_pages(pdf1, headings)
    missing = [h[1] for h in headings if h[2] not in pages and h[1].lower() not in TOC_HEADINGS]
    if missing:
        print("  WARNING: headings not located:", missing)
    # pass 2 (check): page numbers filled in, markers kept, to confirm nothing moved
    doc2, _ = build_html(md_path, pages, markers=True)
    html2 = os.path.join(work, name + ".pass2.html")
    pdf2 = os.path.join(work, name + ".pass2.pdf")
    with open(html2, "w", encoding="utf-8") as f:
        f.write(doc2)
    print_pdf(html2, pdf2, profile)
    pages2 = find_marker_pages(pdf2, headings)
    drift = [h[1] for h in headings if pages.get(h[2]) != pages2.get(h[2])]
    if drift:
        print("  WARNING: page numbers drifted for:", drift)
    # final: same document without the invisible markers (they are absolutely positioned,
    # so removing them does not change the layout)
    doc3, _ = build_html(md_path, pages2, markers=False)
    html3 = os.path.join(work, name + ".html")
    with open(html3, "w", encoding="utf-8") as f:
        f.write(doc3)
    print_pdf(html3, out_pdf, profile)
    print("  %s -> %d pages" % (os.path.basename(out_pdf), page_count(out_pdf)))


if __name__ == "__main__":
    work = os.path.join(os.path.dirname(os.path.abspath(__file__)), "work")
    os.makedirs(work, exist_ok=True)
    for arg in sys.argv[1:]:
        md, pdf = arg.split("=") if "=" in arg else (arg, os.path.splitext(arg)[0] + ".pdf")
        print("Building", os.path.basename(md))
        build(md, pdf, work)
