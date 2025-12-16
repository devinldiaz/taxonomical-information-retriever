import streamlit as st

from utils import get_ncbi_info

parasites = {
    name: data
    for group in st.session_state["DATASETS"].values()
    for name, data in group.items()
}

st.title("ParaSite")
st.caption(
    "Explore curated taxonomical information on parasitic species."
)
st.divider()

st.markdown("## Taxonomic Groups")

st.markdown(
    """
    The following parasite groups are currently curated in this dataset.
    Select a group from the sidebar to explore species-level information.
    """
)

cols = st.columns(2)

groups = [
    ("Digenea", "Flukes", "Trematode parasites with complex life cycles."),
    ("Cestoda", "Tapeworms", "Flatworms inhabiting vertebrate intestines."),
    ("Chromadorea", "Roundworms", "Nematodes including many human pathogens."),
    ("Enoplea", "Whipworms", "Nematodes with diverse hosts."),
]

for col, (name, common, desc) in zip(cols * 2, groups):
    with col:
        st.markdown(f"### {name}")
        st.caption(common)
        st.write(desc)


st.divider()

name = st.text_input(
    "Parasite not listed? Enter the scientific name & search here:"
)

if st.button("Search"):
    info = get_ncbi_info(name)
    st.subheader("NCBI Taxonomical Information")
    if isinstance(info, str):
        st.error(info)
    else:
        st.success(f"**Name:** *{info['Scientific Name']}* ({info['Rank']})")
        st.markdown(f"**Full Lineage:** {info['Lineage']}")

        st.markdown("---")

st.divider()

total_species = sum(len(v) for v in st.session_state["DATASETS"].values())

st.caption(
    f"{total_species}+ curated parasite species • Live taxonomy via NCBI"
)
