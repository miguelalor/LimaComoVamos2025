# Lima Cómo Vamos 2025

Dashboard de la encuesta de percepción sobre calidad de vida urbana de **Lima Cómo Vamos 2025** (1140 encuestas en Lima Metropolitana y Callao, del 5 al 21 de diciembre de 2025; margen de error de ±2.9% en el total y ±6% por área interdistrital). Sigue el design system de Plaza Cívica.

Abre `index.html` desde un servidor local o publícalo con GitHub Pages (rama `main`, carpeta raíz). Los gráficos pueden filtrarse por género, edad, nivel socioeconómico y área interdistrital.

## Estructura

| Ruta | Contenido |
| --- | --- |
| `index.html` | Dashboard listo para publicar, generado por `scripts/build_site.py`. |
| `dashboard/page.html` | Fuente de la página del dashboard (la misma que usa la versión en Claude). |
| `dashboard/shell.html` | Envoltorio independiente: tokens de Plaza Cívica, tema claro y oscuro, y un runtime mínimo que carga los datos. |
| `data/TablasEncuestaLCV2025.xlsx` | Tablas originales de la encuesta. |
| `data/respuestas.json` | Porcentaje por pregunta, tema, respuesta y segmento (0–100), usado por el dashboard. |
| `scripts/parse_tablas.py` | Lee la hoja "Tablas" del Excel y la convierte en JSON por pregunta. |
| `scripts/build_respuestas.py` | Convierte ese JSON en las filas de `data/respuestas.json`. |
| `scripts/build_site.py` | Une `shell.html` y `page.html` en `index.html`. |

## Regenerar

```bash
pip install openpyxl
python scripts/parse_tablas.py data/TablasEncuestaLCV2025.xlsx /tmp/lcv.json
python scripts/build_respuestas.py /tmp/lcv.json data/respuestas.json /tmp/preguntas.json
python scripts/build_site.py
python -m http.server 8000
```

Luego abre <http://localhost:8000>.

Fuente: Lima Cómo Vamos, estudio de percepción sobre calidad de vida urbana 2025.
