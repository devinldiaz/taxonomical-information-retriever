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
    

# Define the pages
main_page = st.Page("home.py", title="Home", icon="🏠")
page_2 = st.Page("digenea.py", title="Digenea", icon="✨")
page_3 = st.Page("cestoda.py", title="Cestoda", icon="✨")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()

