import streamlit as st

from utils import parasite_tab_layout

st.title("Cestoda")

dataset = st.session_state["DATASETS"].get("Cestoda", {})
parasite_tab_layout("Cestoda", dataset)
