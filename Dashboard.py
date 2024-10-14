import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Daftar kecamatan di Bandung
kecamatan_bandung = [
    "Andir", "Astanaanyar", "Antapani", "Arcamanik", "Babakan Ciparay",
    "Bandung Kidul", "Bandung Kulon", "Bandung Wetan", "Batununggal",
    "Bojongloa Kaler", "Bojongloa Kidul", "Buahbatu", "Cibeunying Kaler",
    "Cibeunying Kidul", "Cibiru", "Cicendo", "Cidadap", "Cinambo",
    "Coblong", "Gedebage", "Kiaracondong", "Lengkong", "Mandalajati",
    "Panyileukan", "Rancasari", "Regol", "Sukajadi", "Sukasari", "Sumur Bandung", 
    "Ujungberung"
]

# Sidebar dengan pilihan kecamatan
st.sidebar.title("Kecamatan di Bandung")
kecamatan = st.sidebar.selectbox("Pilih Kecamatan", kecamatan_bandung)

# Logo dan informasi sidebar
logo = "Logo_Bandung-removebg-preview.png"
st.sidebar.image(logo)

# Judul halaman dan deskripsi
st.title(f"Dashboard Bencana Alam - {kecamatan}")

st.markdown(
    """
    Bandung, ibu kota Provinsi Jawa Barat, merupakan salah satu kota terbesar di Indonesia dan dikenal dengan julukan 
    "Kota Kembang" serta "Paris van Java". Kota ini terletak di dataran tinggi dengan cuaca yang sejuk, menjadikannya 
    tujuan favorit wisatawan lokal dan mancanegara. Bandung juga menjadi pusat pendidikan, inovasi, dan industri kreatif di Indonesia.
    """
)

st.header(f"Peta Prediksi Potensi Rentan Banjir di Kecamatan {kecamatan}")

# Menampilkan peta dengan lokasi kecamatan terpilih
m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")

# (Opsional) Tambahkan marker atau overlay khusus berdasarkan kecamatan terpilih
# Misalnya: Folium Marker atau GeoJSON layer
# folium.Marker([latitude, longitude], popup=kecamatan).add_to(m) # Contoh

# Render peta di Streamlit
m.to_streamlit(height=500)
