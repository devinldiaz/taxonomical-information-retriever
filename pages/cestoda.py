import streamlit as st

from utils import parasite_tab_layout

st.title("Cestoda")

parasite_tab_layout("Cestoda", st.session_state["DATASETS"]["Cestoda"])
