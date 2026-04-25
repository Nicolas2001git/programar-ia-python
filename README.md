# DocuSmart IA

DocuSmart IA es una aplicación web desarrollada con **Python** y **Streamlit** que utiliza inteligencia artificial para analizar documentos y extraer información clave automáticamente.

La app permite escribir texto manualmente o subir archivos en formato `.txt`, `.pdf` o `.docx`. Luego, la inteligencia artificial analiza el contenido y devuelve resultados organizados.

---

## Idea del proyecto

La idea base del proyecto puede verse en la siguiente presentación:

[Presentación de la idea del proyecto](https://docs.google.com/presentation/d/1ROT4FKw4VyinipObseuSw2ctK57ldYGDv_X5vVY8qd8/edit?slide=id.g3d580bd0f58_0_89#slide=id.g3d580bd0f58_0_89)

---

## ¿Qué hace la app?

DocuSmart IA analiza documentos y extrae información importante como:

- Categoría
- Subcategoría
- Monto
- Fecha
- Resumen

---

## ¿Cómo funciona?

1. El usuario ingresa su API Key.
2. Escribe un texto o sube un archivo.
3. La app extrae el contenido del documento.
4. La inteligencia artificial analiza el texto.
5. Se muestran los resultados de forma visual.

---

## Formatos aceptados

La aplicación permite subir archivos en los siguientes formatos:

- `.txt`
- `.pdf`
- `.docx`

---

## Tecnologías utilizadas

- Python
- Streamlit
- OpenAI API
- PyPDF
- python-docx

---

## Estructura del proyecto

```bash
IA-PROGRAMACION/
│── index.py
│── README.md
│── requisitos.txt
│── .gitignore

Instalación

Para instalar las dependencias, ejecutar:

pip install -r requisitos.txt
Ejecución

Para iniciar la aplicación, ejecutar:

streamlit run index.py
Modelo utilizado

La aplicación utiliza el modelo:

gpt-4.1-mini

Este modelo permite realizar análisis de texto de forma rápida y con bajo costo.

Prompt utilizado

La aplicación utiliza un prompt estructurado para obtener una salida clara:

Analiza el siguiente texto y responde EXACTAMENTE en este formato:

CATEGORIA: ...
SUBCATEGORIA: ...
MONTO: ...
FECHA: ...
RESUMEN: ...