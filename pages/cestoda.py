import streamlit as st
from utils import parasite_card, get_info, plot_phylogeny

st.title("Cestoda")

plot = plot_phylogeny(
    get_info("Taenia solium")["Lineage"]
)

st.pyplot(plot)