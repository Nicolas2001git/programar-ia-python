# DocuSmart IA

DocuSmart IA es una aplicación desarrollada con **Python** y **Streamlit** que permite analizar texto escrito manualmente o archivos en distintos formatos para extraer información clave de manera automática utilizando la API de OpenAI.

La app está pensada para simplificar la lectura y clasificación de documentos, detectando datos importantes como categoría, subcategoría, montos, fechas y un resumen general del contenido.

## Idea del proyecto

La idea base del proyecto puede verse en la siguiente presentación:

[Presentación de la idea del proyecto](https://docs.google.com/presentation/d/1ROT4FKw4VyinipObseuSw2ctK57ldYGDv_X5vVY8qd8/edit?slide=id.p#slide=id.p)

## Características principales

- Ingreso manual de texto para analizar.
- Carga de archivos en formatos:
  - `.txt`
  - `.pdf`
  - `.docx`
- Extracción automática del contenido del archivo.
- Análisis del documento con inteligencia artificial.
- Detección de:
  - categoría
  - subcategoría
  - montos
  - fechas relevantes
  - resumen del contenido
- Interfaz simple e intuitiva con Streamlit.

## Tecnologías utilizadas

- **Python**
- **Streamlit**
- **OpenAI API**
- **PyPDF**
- **python-docx**

## Estructura del proyecto

```bash
DocuSmart-IA/
│── index.py
│── requirements.txt
│── README.md