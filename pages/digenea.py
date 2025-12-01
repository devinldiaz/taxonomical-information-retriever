import streamlit as st

from utils import parasite_card

st.title("Digenea")

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)


with row1[0]:
    parasite_card(
        "Schistosoma mansoni",
        "",
        "Causes intestinal schistosomiasis in humans",
    )

with row1[1]:
    parasite_card(
        "Schistosoma haematobium",
        "",
        "Causes urinary schistosomiasis in humans"
    )

with row1[2]:
    parasite_card(
        "Schistosoma japonicum",
        "",
        "Causes intestinal schistosomiasis in humans"
    )

with row2[0]:
    parasite_card(
        "Fasciola hepatica",
        "",
        "Causes fascioliasis in livestock and humans"
    )

with row2[1]:
    parasite_card(
        "Clonorchis sinensis",
        "",
        "Causes clonorchiasis in humans"
    )

with row2[2]:
    parasite_card(
        "Paragonimus westermani",
        "",
        "Causes paragonimiasis in humans"
    )

with row3[0]:
    parasite_card(
        "Dicrocoelium dendriticum",
        "",
        "Causes dicrocoeliasis in livestock"
    )

with row3[1]:
    parasite_card(
        "Ribeiroia ondatrae",
        "",
        "Causes limb malformations in amphibians"
    )

with row3[2]:
    parasite_card(
        "Leucochloridium variae",
        "",
        "Infects birds & snails, causing parasitic castration"
    )
