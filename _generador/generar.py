"""Genera el PDF (APA 7) y el Word de las evidencias a partir del Markdown.

Uso (desde la raíz del repositorio):
    python _generador/generar.py            # todas las evidencias del índice del README (menos 10)
    python _generador/generar.py 09 04      # solo las evidencias indicadas

Lee las rutas MD/PDF/Word de la tabla "Índice de evidencias" del README. Los bloques ```mermaid se
convierten en PNG con Mermaid en Chrome antes de generar, sin tocar el Markdown. Ver LEEME.md.
"""
import os, re, sys, subprocess, zipfile
import pypandoc
from playwright.sync_api import sync_playwright

DOCS = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
TOOLS = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(TOOLS, "generador_apa.py")
OUT = os.path.join(TOOLS, "work", "mermaid")
os.makedirs(OUT, exist_ok=True)

# filas del índice del README: carpeta, MD, PDF y Word en ES y EN
readme = open(os.path.join(DOCS, "README.md"), encoding="utf-8").read()
WANT = sys.argv[1:] or ["01", "02", "03", "04", "05", "06", "07", "08", "09", "11"]
JOBS = []
for line in readme.split("\n"):
    m = re.match(r"^\| (\d\d) \|", line)
    if not m or m.group(1) not in WANT:
        continue
    links = re.findall(r"\[(MD|PDF|Word)\]\(([^)]+)\)", line)
    for k in range(0, len(links), 3 if m.group(1) != "11" else 2):
        group = dict(links[k:k + (3 if m.group(1) != "11" else 2)])
        if "MD" in group:
            JOBS.append((group["MD"], group.get("PDF"), group.get("Word")))

HTML = """<!doctype html><html><head><meta charset="utf-8">
<script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
<style>body{margin:0;background:#fff}#c{display:inline-block;padding:12px}</style></head>
<body><div id="c"></div><script>mermaid.initialize({startOnLoad:false,theme:'neutral',fontFamily:'Times New Roman'});</script></body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome", headless=True)
    pg = b.new_page(device_scale_factor=2, viewport={"width": 1400, "height": 1000})
    pg.set_content(HTML); pg.wait_for_function("window.mermaid !== undefined")
    for md, pdf, word in JOBS:
        src = os.path.join(DOCS, md)
        lang = "EN" if "/EN/" in md else "ES"
        text = open(src, encoding="utf-8").read()
        new = text
        tag = re.sub(r"[^A-Za-z0-9]", "_", os.path.basename(md))[:30]
        for n, code in enumerate(re.findall(r"```mermaid\n(.*?)```", text, flags=re.S), 1):
            png = os.path.join(OUT, f"{tag}-{n}.png")
            try:
                svg = pg.evaluate("async (c) => (await mermaid.render('m' + Date.now() + Math.floor(Math.random()*1e6), c)).svg", code)
            except Exception as e:
                print("   ERROR mermaid", md, n, str(e)[:150]); continue
            pg.evaluate("(s) => { document.getElementById('c').innerHTML = s; }", svg)
            pg.locator("#c").screenshot(path=png)
            new = new.replace("```mermaid\n" + code + "```", "![Diagrama](" + png.replace("\\", "/") + ")", 1)
        tmp = os.path.join(os.path.dirname(src), "_tmp_" + os.path.basename(src))
        open(tmp, "w", encoding="utf-8", newline="\n").write(new)
        try:
            if pdf:
                r = subprocess.run([sys.executable, GEN, f"{tmp}={os.path.join(DOCS, pdf)}"], capture_output=True, text=True, cwd=TOOLS)
                print((r.stdout + r.stderr).strip().replace("\n", " | "))
            if word:
                docx = os.path.join(DOCS, word)
                pypandoc.convert_file(tmp, "docx", format="gfm", outputfile=docx,
                                      extra_args=["--reference-doc=" + os.path.join(TOOLS, "estilos", f"referencia_{lang}.docx"), "--resource-path=" + os.path.dirname(src)])
                print("   word", os.path.basename(docx), sum(1 for x in zipfile.ZipFile(docx).namelist() if x.startswith("word/media/")), "imagenes")
        finally:
            os.remove(tmp)
    b.close()
