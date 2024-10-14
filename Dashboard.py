import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Daftar kecamatan di Bandung dan deskripsinya
deskripsi_kecamatan = {
    "Andir": "Andir merupakan wilayah yang terkenal dengan pasar tradisional dan pusat perbelanjaan kain di Kota Bandung.",
    "Astanaanyar": "Astanaanyar memiliki sejarah panjang dengan beberapa situs bersejarah dan menjadi kawasan perumahan yang ramai.",
    "Antapani": "Antapani adalah wilayah pemukiman dengan banyak sekolah dan fasilitas umum yang berkembang.",
    "Arcamanik": "Arcamanik terkenal dengan pusat olahraga, termasuk stadion dan lapangan golf.",
    "Babakan Ciparay": "Babakan Ciparay adalah daerah padat penduduk dengan banyak industri kecil dan perumahan.",
    # Tambahkan deskripsi kecamatan lain sesuai kebutuhan
}

# Sidebar untuk memilih kecamatan
st.sidebar.title("Kecamatan di Bandung")
kecamatan = st.sidebar.selectbox("Pilih Kecamatan", list(deskripsi_kecamatan.keys()))

# Logo dan informasi sidebar
logo = "Logo_Bandung-removebg-preview.png"
st.sidebar.image(logo)

# Judul halaman dan deskripsi dinamis
st.title(f"Dashboard Bencana Alam - {kecamatan}")

st.markdown(
    f"""
    **{kecamatan}**: {deskripsi_kecamatan[kecamatan]}
    """
)

st.header(f"Peta Prediksi Potensi Rentan Banjir di Kecamatan {kecamatan}")

# Menampilkan peta dengan lokasi kecamatan terpilih
m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")

# Render peta di Streamlit
m.to_streamlit(height=500)
