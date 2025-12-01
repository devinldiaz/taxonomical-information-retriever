import streamlit as st

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
    ]
}


# Set up navigation
pg = st.navigation(pages)

# Run the selected page
pg.run()
