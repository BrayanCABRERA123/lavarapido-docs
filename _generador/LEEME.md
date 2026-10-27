# Generador de PDF y Word de las evidencias

Convierte el Markdown de cada evidencia en un PDF con formato APA 7 (Times New Roman 12, doble espacio, márgenes de 1", número de página, tablas y figuras numeradas, referencias con sangría francesa y tabla de contenido con las páginas reales) y en un Word editable.

## Requisitos

- Python 3.11 o superior con `pip install pypandoc_binary playwright` (no hace falta `playwright install`: usa el Chrome instalado).
- Google Chrome en `C:\Program Files\Google\Chrome\Application\chrome.exe`.
- `pdftotext`, que viene con Git para Windows (`C:\Program Files\Git\mingw64\bin\pdftotext.exe`).
- Conexión a internet la primera vez de cada sesión: Mermaid se carga desde jsDelivr (`mermaid@10.9.1`).

Si Chrome o Git están en otra ruta, cambiar `CHROME` y `PDFTOTEXT` al inicio de `generador_apa.py`.

## Uso

Desde la raíz del repositorio:

```
python _generador/generar.py            # todas las evidencias del índice del README, menos el artículo (10)
python _generador/generar.py 09         # solo los manuales
python _generador/generar.py 04 07      # solo diseño e implementación
```

El script lee las rutas MD, PDF y Word de la tabla "Índice de evidencias" del `README.md`, así que una evidencia o un manual nuevo solo necesita su fila en esa tabla. Escribe los PDF y los Word encima de los actuales. Después hay que revisar el resultado y hacer commit.

## Qué hace además del formato APA

Es el generador de los manuales (`build_manuals.py`) con cuatro ajustes, hechos el 27 de octubre de 2026 para regenerar todas las evidencias sin perder contenido:

1. **Diagramas Mermaid.** Cada bloque ` ```mermaid ` se convierte en PNG con Mermaid en Chrome y se inserta como imagen en una copia temporal del Markdown. El Markdown original no se modifica.
2. **Imágenes dentro de tablas.** `![texto](capturas/...)` dentro de una celda se muestra como imagen (antes salía como texto).
3. **Tabla en la portada.** Si la portada (lo que va antes del primer `##`) tiene una tabla, se conserva (matriz de evidencias, 11). Los separadores `---` no se imprimen.
4. **Figuras de una sola página.** Las imágenes tienen un alto máximo de 7,2 pulgadas, para que el título, la imagen y la nota de cada figura queden en la misma página y ninguna se parta.

## Word

El Word se hace con pandoc. Toma los estilos de `estilos/referencia_ES.docx` y `estilos/referencia_EN.docx`, que tienen los estilos de los Word del equipo y ningún contenido.

## Archivos

| Archivo | Para qué sirve |
|---|---|
| `generar.py` | Recorre el índice del README, convierte los diagramas y genera el PDF y el Word de cada documento. |
| `generador_apa.py` | Convierte un Markdown en PDF APA 7 (dos pasadas con Chrome para numerar la tabla de contenido). |
| `apa.css` | Estilos APA del PDF. |
| `estilos/` | Plantillas de estilos del Word (español e inglés). |
| `work/` | Archivos temporales (diagramas y pasadas del PDF); no se sube a Git. |
