import streamlit as st
from openai import OpenAI
from pypdf import PdfReader
from docx import Document
import io
st.set_page_config(page_title="DocuSmart IA")
st.title("DocuSmart IA")

api_key = st.text_input("Ingresá tu OpenAI API Key", type="password")

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

    if not api_key:
        st.warning("Tenés que ingresar tu API Key")
    else:
        client = OpenAI(api_key=api_key)

        texto_final = texto_usuario if texto_usuario.strip() else contenido

        if not texto_final.strip():
            st.warning("Escribí un texto o subí un archivo")
        else:
            prompt = f"""
Eres un asistente especializado en análisis de documentos. Analiza cuidadosamente el siguiente contenido y extrae la información solicitada:

CONTENIDO A ANALIZAR:
{texto_final}

INSTRUCCIONES:
Por favor, proporciona la información en el siguiente formato estructurado:

Si falta algo, poné: No identificado.
📋 CATEGORÍA: [Identifica la categoría principal del documento]
📂 SUBCATEGORÍA: [Especifica la subcategoría correspondiente]
💰 MONTO DETECTADO: [Extrae cualquier cantidad monetaria encontrada]
📅 FECHA DETECTADA: [Identifica fechas relevantes en el documento]
📝 RESUMEN: [Proporciona un resumen conciso del contenido]
"""

            try:
                respuesta = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )

                resultado = respuesta.choices[0].message.content
                st.markdown(resultado)


            except Exception as e:
                st.error(f"Ocurrió un error: {e}")
                print("Hola asdasd ")
            
