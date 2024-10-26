import streamlit as st
import pandas as pd
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

df = pd.read_csv("Dataset_Banjir_Lengkap.csv")  # Ganti nama file jika berbeda

st.write("Data Tiap Wilayah:", df)

deskripsi_kecamatan = {}
for _, row in df.iterrows():

    try:
        lat = float(row["latitude"])
        lon = float(row["longitude"])
        if pd.notnull(lat) and pd.notnull(lon): 
            deskripsi_kecamatan[row["lokasi"]] = {
                "desc": f"Kategori Curah Hujan: {row['Kategori Curah Hujan']}, Labeling: {row['Labeling']}",
                "coords": [lat, lon] 
            }
    except (ValueError, TypeError) as e:
        st.warning(f"Koordinat tidak valid untuk {row['lokasi']}: {row['latitude']}, {row['longitude']}")


st.sidebar.title("Kecamatan di Bandung")
kecamatan = st.sidebar.selectbox("Pilih Kecamatan", ["Semua Kecamatan"] + list(deskripsi_kecamatan.keys()))

logo = "Logo_Bandung-removebg-preview.png"
st.sidebar.image(logo)


st.title(f"Dashboard Bencana Alam - {kecamatan}")

if kecamatan == "Semua Kecamatan":
    st.markdown("**Menampilkan semua kecamatan di Bandung beserta titik koordinatnya.**")
else:
    st.markdown(f"**{kecamatan}**: {deskripsi_kecamatan[kecamatan]['desc']}")

st.header(f"Peta Prediksi Potensi Rentan Banjir di {kecamatan}")

m = leafmap.Map(minimap_control=True, location=[-6.9147, 107.6098], zoom_start=12)  # Fokus ke Bandung
m.add_basemap("OpenTopoMap")

if kecamatan == "Semua Kecamatan":

    for nama, data in deskripsi_kecamatan.items():
        coords = data["coords"]
        if isinstance(coords, list) and len(coords) == 2:  
            st.write(f"Menambahkan marker untuk {nama} di {coords}")  
            m.add_marker(location=coords, popup=f"{nama}: {data['desc']}")
else:
    
    coords = deskripsi_kecamatan.get(kecamatan, {}).get("coords")
    if coords and isinstance(coords, list) and len(coords) == 2:  
        st.write(f"Menambahkan marker untuk {kecamatan} di {coords}")  
        m.add_marker(location=coords, popup=f"{kecamatan}: {deskripsi_kecamatan[kecamatan]['desc']}")


m.to_streamlit(height=500)
