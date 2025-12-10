import streamlit as st

from utils import parasite_tab_layout

st.title("Chromadorea")

if "DATASETS" not in st.session_state:
    st.session_state["DATASETS"] = {}

dataset = st.session_state["DATASETS"].get("Chromadoea", {})
parasite_tab_layout("Chromadorea", dataset)
