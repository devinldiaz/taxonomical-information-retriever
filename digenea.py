import streamlit as st

from utils import parasite_card

st.title("Digenea")

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)


with row1[0]:
    parasite_card(
        "https://www.bioworld.com/ext/resources/BWS/BWS-library/Schistosoma-parasite-infection.webp?",
        "Schistosoma mansoni",
        "Causes intestinal schistosomiasis in humans",
    )

with row1[1]:
    tile = row1[1].container(height=300)
    st.header("Schistosoma haematobium")

with row1[2]:
    tile = row1[2].container(height=300)
    st.header("Schistosoma japonicum")

with row2[0]:
    tile = row2[0].container(height=300)
    st.header("Fasciola hepatica")

with row2[1]:
    tile = row2[1].container(height=300)
    st.header("Clonorchis sinensis")

with row2[2]:
    tile = row2[2].container(height=300)
    st.header("Paragonimus westermani")

with row3[0]:
    tile = row3[0].container(height=300)
    st.header("Dicrocoelium dendriticum")

with row3[1]:
    tile = row3[1].container(height=300)
    st.header("Ribeiroia ondatrae")

with row3[2]:
    title = row3[2].container(height=300)
    st.header("Leucochloridium variae")
