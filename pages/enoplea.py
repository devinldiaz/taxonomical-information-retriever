import streamlit as st

from utils import parasite_tab_layout

st.title("Enoplea")

parasite_tab_layout("Enoplea", st.session_state["DATASETS"]["Enoplea"])
