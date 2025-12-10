import streamlit as st

from utils import parasite_tab_layout

st.title("Digenea")

parasite_tab_layout("Digenea", st.session_state["DATASETS"]["Digenea"])
