import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Daftar kecamatan di Bandung dan deskripsinya
deskripsi_kecamatan = {
    "Andir": "Andir terkenal dengan pusat tekstil dan beberapa pasar grosir di Bandung.",
    "Astanaanyar": "Astanaanyar memiliki sejarah panjang dan terkenal dengan kawasan perumahan serta perkantoran.",
    "Antapani": "Antapani adalah wilayah pemukiman dengan banyak sekolah dan fasilitas umum.",
    "Arcamanik": "Arcamanik terkenal dengan stadion olahraga dan lapangan golf.",
    "Babakan Ciparay": "Babakan Ciparay adalah daerah padat penduduk dengan aktivitas perdagangan dan industri kecil.",
    "Bandung Kidul": "Bandung Kidul dikenal sebagai area perumahan dengan komunitas yang beragam.",
    "Bandung Kulon": "Bandung Kulon memiliki banyak kawasan industri dan pusat kegiatan ekonomi.",
    "Bandung Wetan": "Bandung Wetan merupakan pusat komersial dan perkantoran, dekat dengan pusat kota.",
    "Batununggal": "Batununggal adalah area perumahan dengan beberapa kompleks perumahan modern.",
    "Bojongloa Kaler": "Bojongloa Kaler dikenal dengan pasar tradisional dan kawasan perumahan.",
    "Bojongloa Kidul": "Bojongloa Kidul merupakan area yang berkembang dengan banyak pusat perdagangan.",
    "Buahbatu": "Buahbatu adalah wilayah yang berkembang pesat dengan banyak tempat makan dan perumahan.",
    "Cibeunying Kaler": "Cibeunying Kaler memiliki banyak ruang terbuka hijau dan kawasan kampus.",
    "Cibeunying Kidul": "Cibeunying Kidul dikenal sebagai kawasan pemukiman yang asri.",
    "Cibiru": "Cibiru merupakan area yang berkembang dengan beberapa kampus dan pusat pendidikan.",
    "Cicendo": "Cicendo dikenal sebagai kawasan pusat transportasi dan komersial.",
    "Cidadap": "Cidadap terkenal dengan kawasan wisata alam dan perumahan elit.",
    "Cinambo": "Cinambo merupakan area yang berkembang dengan pusat perumahan baru.",
    "Coblong": "Coblong memiliki kawasan pendidikan dan komersial yang aktif.",
    "Gedebage": "Gedebage dikenal dengan stadion dan pusat olahraga di Bandung.",
    "Kiaracondong": "Kiaracondong adalah kawasan industri dan komersial dengan akses transportasi mudah.",
    "Lengkong": "Lengkong merupakan area pemukiman dan pusat pendidikan.",
    "Mandalajati": "Mandalajati memiliki banyak kawasan hijau dan area perumahan.",
    "Panyileukan": "Panyileukan dikenal dengan perumahan modern dan pusat pendidikan.",
    "Rancasari": "Rancasari merupakan area industri dan pemukiman.",
    "Regol": "Regol dikenal dengan kawasan budaya dan sejarah.",
    "Sukajadi": "Sukajadi merupakan pusat perbelanjaan dan perdagangan.",
    "Sukasari": "Sukasari memiliki banyak tempat makan dan pusat perbelanjaan.",
    "Sumur Bandung": "Sumur Bandung adalah pusat kota dengan banyak gedung bersejarah dan pusat komersial.",
    "Ujungberung": "Ujungberung merupakan kawasan perumahan dan pusat kegiatan seni."
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
