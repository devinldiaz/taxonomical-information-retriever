import streamlit as st

from utils import parasite_tab_layout

st.title("Enoplea")

dataset = st.session_state["DATASETS"].get("Enoplea", {})
parasite_tab_layout("Enoplea", dataset)
