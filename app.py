import streamlit as st
import os

st.title("Diagnostic")

st.write("Racine :", os.listdir("."))

if os.path.exists("modules"):
    st.write("Modules :", os.listdir("modules"))
else:
    st.error("Dossier modules introuvable")
