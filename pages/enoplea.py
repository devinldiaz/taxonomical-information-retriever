import streamlit as st

from utils import parasite_tab_layout

st.title("Enoplea")

if "DATASETS" not in st.session_state:
    st.session_state["DATASETS"] = {}

dataset = st.session_state["DATASETS"].get("Enoplea", {})
parasite_tab_layout("Enoplea", dataset)
