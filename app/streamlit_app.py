import streamlit as st
import pandas as pd
import joblib
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Predição de Zoonoses Brasil", layout="wide")

st.title("🦠 Dashboard de Predição de Zoonoses")
st.markdown("""
Este painel apresenta as predições de surtos de zoonoses baseadas em dados climáticos e sanitários.
""")

# Sidebar for controls
st.sidebar.header("Configurações")
disease = st.sidebar.selectbox("Selecione a Doença", ["Leptospirose", "Leishmaniose"])
horizon = st.sidebar.slider("Horizonte de Predição (Meses)", 1, 3, 1)

# Logic placeholder
st.info("Carregando dados e modelo preditivo...")

# Footer
st.markdown("---")
st.caption("Desenvolvido para o projeto Predição de Zoonoses Brasil.")
