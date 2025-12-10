import streamlit as st

from utils import parasite_tab_layout

st.title("Chromadorea")

parasite_tab_layout("Chromadorea", st.session_state["DATASETS"]["Chromadorea"])
