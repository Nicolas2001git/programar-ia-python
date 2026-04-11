import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from pypdf import PdfReader
from docx import Document
import os
import io

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="DocuSmart IA")
st.title("DocuSmart IA")

texto_usuario = st.text_area("Escribí un texto")

archivo = st.file_uploader("O subí un archivo", type=["txt", "pdf", "docx"])

contenido = ""

if archivo is not None:
    if archivo.name.endswith(".txt"):
        contenido = archivo.read().decode("utf-8", errors="ignore")

    elif archivo.name.endswith(".pdf"):
        pdf = PdfReader(io.BytesIO(archivo.read()))
        for pagina in pdf.pages:
            contenido += (pagina.extract_text() or "") + "\n"

    elif archivo.name.endswith(".docx"):
        doc = Document(io.BytesIO(archivo.read()))
        for p in doc.paragraphs:
            contenido += p.text + "\n"

if st.button("Analizar"):
    texto_final = texto_usuario if texto_usuario.strip() else contenido

    if not texto_final.strip():
        st.warning("Escribí un texto o subí un archivo")
    else:
        prompt = f"""
Analiza este contenido:

{texto_final}

Con eso respondé así:
Categoría:
Subcategoría:
Monto detectado:
Fecha detectada:
Resumen:

Si falta algo, poné: No identificado.
"""

        try:
            respuesta = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            resultado = respuesta.choices[0].message.content
            st.write(resultado)

        except Exception as e:
            st.error(f"Ocurrió un error: {e}")