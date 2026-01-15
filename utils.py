import os
from collections import Counter

import matplotlib.pyplot as plt
import streamlit as st
from Bio import Entrez
from dotenv import load_dotenv

from data import cestoda, chromadorea, digenea, enoplea

load_dotenv()

Entrez.email = os.getenv("NCBI_EMAIL")

if "DATASETS" not in st.session_state:
    st.session_state["DATASETS"] = {
        "Digenea": digenea,
        "Cestoda": cestoda,
        "Chromadorea": chromadorea,
        "Enoplea": enoplea,
    }


def get_ncbi_info(name):
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
            "Taxonomy ID": tax_id,
            "Taxonomy URL":
            f"https://www.ncbi.nlm.nih.gov/datasets/taxonomy/{tax_id}/",
            "Lineage": full_lineage,
        }
    except Exception as e:
        return f"NCBI error: {e}"


def parasite_card(name, data):
    if data.get("image") is None:
        data["image"] = "images/placeholder.jpg"
    st.image(data.get("image"), width="stretch")

    @st.dialog(f"More about {name}")
    def show_details():
        st.write(data.get("description", ""))

        if "taxonomy" in data:
            st.subheader("Taxonomy")
            st.json(data["taxonomy"])

        if "hosts" in data:
            st.subheader("Hosts")
            st.write(", ".join(data["hosts"]))

        ncbi = get_ncbi_info(name)
        if isinstance(ncbi, dict):
            st.subheader("NCBI Genome Link: ")
            st.markdown(f"[Genome link]({ncbi['Taxonomy URL']})")
            with st.container(border=True):
                st.subheader("NCBI Taxonomy")
                st.json(ncbi)

                if "Lineage" in ncbi:
                    fig = plot_phylogeny(ncbi["Lineage"])
                    st.pyplot(fig)

    # Clicking button opens the dialog
    if st.button(f"More about {name}", key=f"btn_{name}"):
        show_details()


def parasite_grid(dataset):
    names = list(dataset.keys())
    cols = st.columns(3)

    for idx, name in enumerate(names):
        with cols[idx % 3]:
            parasite_card(name, dataset[name])


def overview_tab(title, dataset):
    st.write(f"### Overview of {title}")
    if not dataset:
        st.info("No species data available.")
        return

    col1, col2, col3 = st.columns(3)

    col1.metric("Species in dataset", len(dataset))
    all_hosts = [
        host
        for parasite in dataset.values()
        for host in parasite.get("hosts", [])
    ]
    col2.metric("Unique hosts", len(set(all_hosts)))

    orders = [
        parasite.get("taxonomy", {}).get("order", "Unknown")
        for parasite in dataset.values()
    ]
    col3.metric("Orders represented", len(set(orders)))


def parasite_tab_layout(title, dataset):
    tab1, tab2, tab3 = st.tabs(["Overview", "Species", "More"])

    with tab1:
        overview_tab(title, dataset)

    with tab2:
        parasite_grid(dataset)

    with tab3:
        st.write("tbd")


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
