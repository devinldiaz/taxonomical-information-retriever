import streamlit as st

from utils import get_info

st.title("Taxonomical Information Retriever")

name = st.text_input("Enter the scientific name of an organism:")

if st.button("Search"):
    info = get_info(name)
    st.header("NCBI Taxonomical Information")
    if isinstance(info, str):
        st.error(info)
    else:
        st.success(f"**Name:** *{info['Scientific Name']}* ({info['Rank']})")
        st.markdown(f"**Taxonomy ID:** `{info['Taxonomy ID']}`")
        st.markdown(f"**Full Lineage:** {info['Lineage']}")

        st.markdown("---")
