import streamlit as st
import main

st.title("Taxonomical Information Retriever")

name = st.text_input("Enter the scientific name of an organism:")

if st.button("Search"):
    info = main.get_info(name)
    st.header("NCBI Taxonomical Information")
    if isinstance(info, str):
        st.error(info)
    else:
        st.success(f"**Name Found:** *{info['Scientific Name']}* ({info['Rank'].capitalize()})")
        st.markdown(f"**Taxonomy ID:** `{info['Taxonomy ID']}`")
        st.markdown(f"**Full Lineage:** {info['Lineage']}")
        
        st.markdown('---')