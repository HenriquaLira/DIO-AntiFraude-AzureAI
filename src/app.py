import streamlit as st

def configure_interface():
    st.title("Upload de arquivos DIO - Desafio 1 - Azure - Fake Docs")
    upload_file = st.file_uploader("Escolha um arquivo", type={})