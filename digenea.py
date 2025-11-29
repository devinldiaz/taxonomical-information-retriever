import streamlit as st
from streamlit_extras.let_it_rain import rain
import main
st.title("Digenea")

# create many containers for several cards, each with heading, a search button, photo, and text. and the button will return relevant info
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
# for col in row:
#     
#     tile = col.container(height = 300)


with row1[0]:
    # st.html("<p style='background-color: red'>it's working</p>");
    tile = row1[0].container(height = 300)
    st.header("Schistosoma mansoni")

    with tile:
        st.image("https://www.ncbi.nlm.nih.gov/Taxonomy/taxi/images/4049", width=150)
        st.write("This is an example card with an image and some text.")
        if st.button("S. mansoni taxonomy information"):
            info = main.get_info("Schistosoma mansoni")
            st.header("NCBI Taxonomical Information")
            if isinstance(info, str):
                st.error(info)
            else:
                st.balloons()
                st.success(f"**Name Found:** *{info['Scientific Name']}* ({info['Rank'].capitalize()})")
                st.markdown(f"**Taxonomy ID:** `{info['Taxonomy ID']}`")
                st.markdown(f"**Full Lineage:** {info['Lineage']}")
                st.markdown('---')
            

with row1[1]:
    tile = row1[1].container(height = 300)
    st.header("Schistosoma haematobium")

with row1[2]:
    tile = row1[2].container(height = 300)
    st.header("Schistosoma japonicum")

with row2[0]:
    tile = row2[0].container(height = 300)
    st.header("Fasciola hepatica")

with row2[1]:
    tile = row2[1].container(height = 300)
    st.header("Clonorchis sinensis")

with row2[2]:
    tile = row2[2].container(height = 300)
    st.header("Paragonimus westermani")

with row3[0]:
    tile = row3[0].container(height = 300)
    st.header("Dicrocoelium dendriticum")

with row3[1]:
    tile = row3[1].container(height = 300)
    st.header("Ribeiroia ondatrae")

with row3[2]:
    title = row3[2].container(height = 300)
    st.header("Leucochloridium variae")