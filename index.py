import streamlit as st
from openai import OpenAI
from pypdf import PdfReader
from docx import Document
import io

st.set_page_config(page_title="DocuSmart IA", layout="wide")

st.markdown("""
<style>

.main-title {
    font-size: 38px;
    font-weight: 700;
    color: #1D3557;
    margin-bottom: 5px;
}

.secondary-title {
    font-size: 18px;
    color: #555555;
    margin-bottom: 20px;
}

.box {
    background-color: #F8F9FA;
    padding: 16px;
    border-radius: 12px;
    border: 1px solid #E9ECEF;
    margin-bottom: 16px;
}

.box-title {
    font-size: 16px;
    font-weight: 600;
    margin-bottom: 6px;
}

.result-card {
    background-color: #FFFFFF;
    padding: 14px;
    border-radius: 10px;
    border: 1px solid #E0E0E0;
    margin-bottom: 12px;
}

.result-label {
    font-size: 13px;
    color: #777777;
    margin-bottom: 4px;
}

.result-value {
    font-size: 16px;
    font-weight: 600;
    color: #1D3557;
}

</style>
""", unsafe_allow_html=True)


def extraer_texto_archivo(archivo):
    contenido = ""

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

    return contenido

with st.sidebar:
    st.header("ℹ️ Información")
    st.write("DocuSmart IA analiza documentos automáticamente.")
    st.write("Formatos: TXT, PDF, DOCX")


st.markdown('<div class="main-title">DocuSmart IA</div>', unsafe_allow_html=True)
st.markdown('<div class="secondary-title">Analizá documentos con inteligencia artificial</div>', unsafe_allow_html=True)

st.markdown("""
<div class="box">
    <p class="box-title">¿Qué hace esta app?</p>
    <p>Analiza documentos y extrae información clave automáticamente.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="box">
    <p class="box-title">¿Cómo funciona?</p>
    <p>1. Ingresás tu API Key</p>
    <p>2. Subís o escribís contenido</p>
    <p>3. La IA analiza el documento</p>
    <p>4. Recibís resultados estructurados</p>
</div>
""", unsafe_allow_html=True)

st.subheader("Ingreso de información")

api_key = st.text_input("API Key", type="password")
texto_usuario = st.text_area("Texto", height=180)
archivo = st.file_uploader("Archivo", type=["txt", "pdf", "docx"])

contenido = ""
if archivo:
    contenido = extraer_texto_archivo(archivo)

    st.subheader("Texto detectado")
    st.text_area("Vista previa", contenido, height=200, disabled=True)


if st.button("Analizar documento"):

    if not api_key:
        st.warning("Ingresá la API Key")
    else:
        texto_final = texto_usuario if texto_usuario.strip() else contenido

        if not texto_final.strip():
            st.warning("Ingresá texto o archivo")
        else:
            try:
                client = OpenAI(api_key=api_key)

                prompt = f"""
Analiza el siguiente texto y responde EXACTAMENTE en este formato:

CATEGORIA: ...
SUBCATEGORIA: ...
MONTO: ...
FECHA: ...
RESUMEN: ...

Texto:
{texto_final}
"""

                with st.spinner("Analizando..."):
                    respuesta = client.chat.completions.create(
                        model="gpt-4.1-mini",
                        messages=[{"role": "user", "content": prompt}]
                    )

                resultado = respuesta.choices[0].message.content

                def extraer(campo):
                    for linea in resultado.split("\n"):
                        if campo in linea:
                            return linea.split(":",1)[1].strip()
                    return "No identificado"

                categoria = extraer("CATEGORIA")
                subcategoria = extraer("SUBCATEGORIA")
                monto = extraer("MONTO")
                fecha = extraer("FECHA")
                resumen = extraer("RESUMEN")

                st.success("Análisis completado")

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown(f"""
                    <div class="result-card">
                        <div class="result-label">Categoría</div>
                        <div class="result-value">{categoria}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown(f"""
                    <div class="result-card">
                        <div class="result-label">Monto</div>
                        <div class="result-value">{monto}</div>
                    </div>
                    """, unsafe_allow_html=True)

                with col2:
                    st.markdown(f"""
                    <div class="result-card">
                        <div class="result-label">Subcategoría</div>
                        <div class="result-value">{subcategoria}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown(f"""
                    <div class="result-card">
                        <div class="result-label">Fecha</div>
                        <div class="result-value">{fecha}</div>
                    </div>
                    """, unsafe_allow_html=True)
                st.markdown(f"""
                <div class="box">
                    <p class="box-title">Resumen</p>
                    <p>{resumen}</p>
                </div>
                """, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error: {e}")