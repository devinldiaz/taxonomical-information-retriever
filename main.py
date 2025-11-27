import re
import streamlit as st
from Bio import Entrez
from dotenv import load_dotenv
import os

load_dotenv()

Entrez.email = os.getenv("NCBI_EMAIL")

def get_info(name):
    try:
        handle = Entrez.esearch(db="taxonomy", term=name)
        record = Entrez.read(handle)
        handle.close()

        if not record["IdList"]:
            return "No match found in NCBI Taxonomy."
        
        tax_id = record["IdList"][0]
        handle = Entrez.efetch(db="taxonomy", id=tax_id, retmode="xml")
        tax_record = Entrez.read(handle)
        handle.close()

        scientific_name = tax_record[0]["ScientificName"]
        rank = tax_record[0]["Rank"]
        lineage = tax_record[0]["LineageEx"]

        full_lineage = " > ".join([item['ScientificName'] for item in lineage])

        return{
            "Scientific Name": scientific_name,
            "Rank": rank,
            "Taxonomy ID": tax_id,
            "Lineage": full_lineage
        }
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None
    

st.title("Taxonomical Information Retriever")

name = st.text_input("Enter the scientific name of an organism:")

if st.button("Search"):
    info = get_info(name)
    st.header("NCBI Taxonomical Information")
    if isinstance(info, str):
        st.error(info)
    else:
        st.success(f"**Name Found:** *{info['Scientific Name']}* ({info['Rank'].capitalize()})")
        st.markdown(f"**Taxonomy ID:** `{info['Taxonomy ID']}`")
        st.markdown(f"**Full Lineage:** {info['Lineage']}")
        
        st.markdown('---')