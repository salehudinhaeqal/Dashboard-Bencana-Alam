import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Jawa Barat
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "Logo_Bandung-removebg-preview.png"
st.sidebar.image(logo)

# Customize page title
st.title("Dashboard Bencana Alam Kota Bandung")

st.markdown(
    """
    Bandung, ibu kota Provinsi Jawa Barat, merupakan salah satu kota terbesar di Indonesia dan dikenal dengan julukan "Kota Kembang" serta "Paris van Java". Kota ini terletak di dataran tinggi dengan cuaca yang sejuk, menjadikannya tujuan favorit wisatawan lokal dan mancanegara. Bandung juga menjadi pusat pendidikan, inovasi, dan industri kreatif di Indonesia.
    """
)

st.header("Peta Prediksi Potensi Rentan Banjir Kota Bandung")

markdown = """


"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)