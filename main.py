import streamlit as st

from data import cestoda, chromadorea, digenea, enoplea

if "DATASETS" not in st.session_state:
    st.session_state["DATASETS"] = {
        "Digenea": digenea,
        "Cestoda": cestoda,
        "Chromadorea": chromadorea,
        "Enoplea": enoplea
    }

pages = {
    "Home": [
        st.Page("pages/home.py", title="Home", icon="🏠")
    ],
    "Phylum Platyhelminthes": [
        st.Page("pages/digenea.py", title="Digenea", icon="✨"),
        st.Page("pages/cestoda.py", title="Cestoda", icon="✨")
    ],
    "Phylum Nematoda": [
        st.Page("pages/chromadorea.py", title="Chromadorea", icon="✨"),
        st.Page("pages/enoplea.py", title="Enoplea", icon="✨")
    ]
}

# Set up navigation
pg = st.navigation(pages)

# Run the selected page
pg.run()
