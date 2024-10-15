import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Daftar kecamatan di Bandung beserta deskripsi dan koordinatnya
deskripsi_kecamatan = {
    "Andir": {"desc": "Pusat tekstil dan pasar grosir.", "coords": [-6.9149, 107.5924]},
    "Astanaanyar": {"desc": "Kawasan perumahan dan perkantoran.", "coords": [-6.9285, 107.6037]},
    "Antapani": {"desc": "Wilayah pemukiman dengan banyak sekolah.", "coords": [-6.9147, 107.6572]},
    "Arcamanik": {"desc": "Dikenal dengan stadion dan lapangan golf.", "coords": [-6.9025, 107.6794]},
    "Babakan Ciparay": {"desc": "Daerah padat dengan industri kecil.", "coords": [-6.9474, 107.5789]},
    "Bandung Kidul": {"desc": "Area perumahan dengan komunitas beragam.", "coords": [-6.9615, 107.6348]},
    "Bandung Kulon": {"desc": "Pusat industri dan kegiatan ekonomi.", "coords": [-6.9267, 107.5733]},
    "Bandung Wetan": {"desc": "Pusat komersial dan perkantoran.", "coords": [-6.9115, 107.6266]},
    "Batununggal": {"desc": "Area dengan perumahan modern.", "coords": [-6.9437, 107.6282]},
    "Bojongloa Kaler": {"desc": "Dikenal dengan pasar tradisional.", "coords": [-6.9263, 107.5897]},
    "Bojongloa Kidul": {"desc": "Kawasan perdagangan berkembang.", "coords": [-6.9454, 107.6036]},
    "Buahbatu": {"desc": "Wilayah dengan banyak tempat makan.", "coords": [-6.9606, 107.6404]},
    "Cibeunying Kaler": {"desc": "Memiliki ruang hijau dan kampus.", "coords": [-6.8861, 107.6362]},
    "Cibeunying Kidul": {"desc": "Kawasan pemukiman asri.", "coords": [-6.9031, 107.6367]},
    "Cibiru": {"desc": "Area dengan beberapa kampus.", "coords": [-6.9174, 107.7194]},
    "Cicendo": {"desc": "Kawasan transportasi dan komersial.", "coords": [-6.9018, 107.5979]},
    "Cidadap": {"desc": "Kawasan wisata alam dan elit.", "coords": [-6.8583, 107.6031]},
    "Cinambo": {"desc": "Pusat perumahan baru.", "coords": [-6.9086, 107.7105]},
    "Coblong": {"desc": "Kawasan pendidikan dan komersial.", "coords": [-6.8903, 107.6167]},
    "Gedebage": {"desc": "Dikenal dengan stadion olahraga.", "coords": [-6.9480, 107.7228]},
    "Kiaracondong": {"desc": "Kawasan industri dan transportasi.", "coords": [-6.9319, 107.6432]},
    "Lengkong": {"desc": "Area pemukiman dan pusat pendidikan.", "coords": [-6.9282, 107.6246]},
    "Mandalajati": {"desc": "Memiliki banyak kawasan hijau.", "coords": [-6.8766, 107.6667]},
    "Panyileukan": {"desc": "Perumahan modern dan pusat pendidikan.", "coords": [-6.9431, 107.7185]},
    "Rancasari": {"desc": "Area industri dan pemukiman.", "coords": [-6.9600, 107.6818]},
    "Regol": {"desc": "Kawasan budaya dan sejarah.", "coords": [-6.9285, 107.6064]},
    "Sukajadi": {"desc": "Pusat perbelanjaan dan perdagangan.", "coords": [-6.8830, 107.5837]},
    "Sukasari": {"desc": "Banyak tempat makan dan belanja.", "coords": [-6.8737, 107.5939]},
    "Sumur Bandung": {"desc": "Pusat kota dengan gedung bersejarah.", "coords": [-6.9128, 107.6079]},
    "Ujungberung": {"desc": "Perumahan dan pusat seni.", "coords": [-6.9173, 107.7178]}
}

# Sidebar untuk memilih kecamatan, termasuk opsi 'Semua Kecamatan'
st.sidebar.title("Kecamatan di Bandung")
kecamatan = st.sidebar.selectbox("Pilih Kecamatan", ["Semua Kecamatan"] + list(deskripsi_kecamatan.keys()))

# Logo dan informasi sidebar
logo = "Logo_Bandung-removebg-preview.png"
st.sidebar.image(logo)

# Judul halaman dan deskripsi dinamis
st.title(f"Dashboard Bencana Alam - {kecamatan}")

if kecamatan == "Semua Kecamatan":
    st.markdown("**Menampilkan semua kecamatan di Bandung beserta titik koordinatnya.**")
else:
    st.markdown(f"**{kecamatan}**: {deskripsi_kecamatan[kecamatan]['desc']}")

st.header(f"Peta Prediksi Potensi Rentan Banjir di {kecamatan}")

# Menampilkan peta dan marker
m = leafmap.Map(minimap_control=True, location=[-6.9147, 107.6098], zoom_start=12)  # Fokus ke Bandung
m.add_basemap("OpenTopoMap")

if kecamatan == "Semua Kecamatan":
    # Tambahkan marker untuk semua kecamatan
    for nama, data in deskripsi_kecamatan.items():
        m.add_marker(location=data["coords"], popup=f"{nama}: {data['coords']}")
else:
    # Tambahkan marker hanya untuk kecamatan terpilih
    coords = deskripsi_kecamatan[kecamatan]["coords"]
    m.add_marker(location=coords, popup=f"{kecamatan}: {coords}")

# Render peta di Streamlit
m.to_streamlit(height=500)
