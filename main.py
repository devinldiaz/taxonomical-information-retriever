import streamlit as st

main_page = st.Page("home.py", title="Home", icon="🏠")
page_2 = st.Page("digenea.py", title="Digenea", icon="✨")
page_3 = st.Page("cestoda.py", title="Cestoda", icon="✨")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()

