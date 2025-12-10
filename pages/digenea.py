import streamlit as st

from utils import parasite_tab_layout

st.title("Digenea")

dataset = st.session_state["DATASETS"].get("Digenea", {})
parasite_tab_layout("Digenea", dataset)
