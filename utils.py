import os

import matplotlib.pyplot as plt
import streamlit as st
from Bio import Entrez
from dotenv import load_dotenv

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

        full_lineage = " > ".join([item["ScientificName"] for item in lineage])

        return {
            "Scientific Name": scientific_name,
            "Rank": rank,
            # "Taxonomy ID": tax_id,
            "Lineage": full_lineage,
        }
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None


def parasite_card(image_url, parasite_name, description=""):
    with st.container(border=True):
        st.subheader(parasite_name)
        st.image(image_url, width=250)
        if description:
            st.write(description)

        if st.button(
            f"{parasite_name} taxonomy information", key=f"{parasite_name}_btn"
        ):
            info = get_info(parasite_name)

            st.header("NCBI Taxonomical Information")

            if isinstance(info, str):
                st.error(info)
            else:
                st.success(f"**Name:** *{info['Scientific Name']}*({info['Rank']})")
                # st.markdown(f"**Taxonomy ID:** `{info['Taxonomy ID']}`")
                st.markdown(f"**Full Lineage:** {info['Lineage']}")
                st.markdown("---")
    return None


def plot_phylogeny(lineage_string):
    lineage = lineage_string.split(" > ")

    fig, ax = plt.subplots(figsize=(4, 6))

    y_start = 1.0
    y_step = 0.1

    for i, node in enumerate(lineage):
        y = y_start - i * y_step
        ax.text(0.1, y, node, fontsize=10, verticalalignment="center")
        if i > 0:
            y_prev = y_start - (i - 1) * y_step
            ax.plot([0.05, 0.05], [y_prev, y], linewidth=2)

    ax.axis("off")
    return fig
