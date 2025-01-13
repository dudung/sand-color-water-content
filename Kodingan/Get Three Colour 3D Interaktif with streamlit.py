import streamlit as st
from colorthief import ColorThief
import plotly.graph_objects as go

# Judul aplikasi
st.title("Dashboard Analisis Warna Dominan")
st.sidebar.header("Pengaturan")

# Daftar file gambar
num_images = st.sidebar.slider("Jumlah Gambar", 1, 18, 10)  # Atur jumlah gambar dinamis
image_files = [f"W{i}.png" for i in range(num_images)]

# Fungsi untuk mendapatkan warna dominan
@st.cache
def get_dominant_color(image_file):
    ct = ColorThief(image_file)
    return ct.get_color(quality=1)

# Ambil warna dominan dari masing-masing gambar
dominant_colors = [get_dominant_color(image) for image in image_files]

# Terapkan skala untuk memperbesar perbedaan koordinat
scale_factor = st.sidebar.slider("Skala RGB", 1, 10, 1)
scaled_colors = [(r * scale_factor, g * scale_factor, b * scale_factor) for r, g, b in dominant_colors]

# Identifikasi gambar dengan koordinat RGB tereskalasi yang sama
color_map = {}
duplicates = []

for i, scaled in enumerate(scaled_colors):
    if scaled in color_map:
        duplicates.append((color_map[scaled], i + 1))  # Simpan pasangan gambar duplikat
    else:
        color_map[scaled] = i + 1

# Tampilkan informasi warna
st.subheader("Informasi Warna Dominan")
color_data = []
for i, (original, scaled) in enumerate(zip(dominant_colors, scaled_colors)):
    hex_color = f"#{original[0]:02x}{original[1]:02x}{original[2]:02x}"
    color_data.append({"Gambar": f"W{i+1}", "RGB": original, "HEX": hex_color, "Scaled RGB": scaled})

st.write(color_data)

# Tampilkan hasil duplikasi
if duplicates:
    st.warning("Gambar-gambar dengan warna tereskalasi yang sama ditemukan:")
    for dup1, dup2 in duplicates:
        st.write(f"Gambar {dup1} dan Gambar {dup2}")
else:
    st.success("Tidak ada gambar dengan warna tereskalasi yang sama.")

# Plot dalam grafik 3D menggunakan Plotly
st.subheader("Visualisasi 3D Warna Dominan")
fig = go.Figure()

for i, (scaled, original) in enumerate(zip(scaled_colors, dominant_colors)):
    r, g, b = scaled
    hex_color = f"#{original[0]:02x}{original[1]:02x}{original[2]:02x}"
    fig.add_trace(go.Scatter3d(
        x=[r], y=[g], z=[b],
        mode='markers+text',
        marker=dict(size=8, color=hex_color),
        text=[f"W{i}"],
        textposition="top center"
    ))

fig.update_layout(scene=dict(
    xaxis_title='Red',
    yaxis_title='Green',
    zaxis_title='Blue'
), title="Perbandingan Warna Dominan")

st.plotly_chart(fig)
