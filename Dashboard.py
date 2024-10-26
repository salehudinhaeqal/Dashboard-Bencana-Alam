import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Membaca file CSV hasil labeling
df = pd.read_csv("Dataset_Banjir_Lengkap.csv")  # Ganti nama file jika berbeda

# Debugging: Tampilkan data yang dibaca
st.write("Data yang dibaca:", df)

# Mengonversi data CSV menjadi struktur dictionary
deskripsi_kecamatan = {}
for _, row in df.iterrows():
    # Pastikan latitude dan longitude tidak kosong
    if pd.notnull(row["latitude"]) and pd.notnull(row["longitude"]):
        deskripsi_kecamatan[row["lokasi"]] = {
            "desc": f"Kategori Curah Hujan: {row['Kategori Curah Hujan']}, Labeling: {row['Labeling']}",
            "coords": [float(row["latitude"]), float(row["longitude"])]  # Pastikan tipe data float
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
        coords = data["coords"]
        if isinstance(coords, list) and len(coords) == 2:  # Pastikan koordinat valid
            st.write(f"Menambahkan marker untuk {nama} di {coords}")  # Debugging: Tampilkan informasi marker
            m.add_marker(location=coords, popup=f"{nama}: {data['desc']}")
else:
    # Tambahkan marker hanya untuk kecamatan terpilih
    coords = deskripsi_kecamatan.get(kecamatan, {}).get("coords")
    if coords and isinstance(coords, list) and len(coords) == 2:  # Pastikan koordinat valid
        st.write(f"Menambahkan marker untuk {kecamatan} di {coords}")  # Debugging: Tampilkan informasi marker
        m.add_marker(location=coords, popup=f"{kecamatan}: {deskripsi_kecamatan[kecamatan]['desc']}")

# Render peta di Streamlit
m.to_streamlit(height=500)
