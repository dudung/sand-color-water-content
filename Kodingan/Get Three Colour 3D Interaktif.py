from colorthief import ColorThief
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Daftar file gambar
image_files = [f"W{i}_gelap.png" for i in range(0, 18)]

# Fungsi untuk mendapatkan warna dominan
def get_dominant_color(image_file):
    ct = ColorThief(image_file)
    return ct.get_color(quality=1)

# Ambil warna dominan dari masing-masing gambar
dominant_colors = [get_dominant_color(image) for image in image_files]

# Terapkan skala untuk memperbesar perbedaan koordinat
scale_factor = 1  # Ubah ini untuk memperbesar/memperkecil jarak
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
for i, (original, scaled) in enumerate(zip(dominant_colors, scaled_colors)):
    hex_color = f"#{original[0]:02x}{original[1]:02x}{original[2]:02x}"
    print(f"Gambar {i+1} - Dominan RGB: {original}, HEX: {hex_color}, Scaled RGB: {scaled}")

# Tampilkan hasil duplikasi
if duplicates:
    print("\nGambar-gambar dengan warna tereskalasi yang sama:")
    for dup1, dup2 in duplicates:
        print(f"Gambar {dup1} dan Gambar {dup2}")
else:
    print("\nTidak ada gambar dengan warna tereskalasi yang sama.")

# Plot dalam grafik 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot setiap warna dengan koordinat tereskalasi
import plotly.graph_objects as go

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

fig.show()


# Atur label dan judul grafik
ax.set_xlabel("Red (scaled)")
ax.set_ylabel("Green (scaled)")
ax.set_zlabel("Blue (scaled)")
ax.set_title("Perbandingan Warna Dominan dengan Perbedaan yang Ditingkatkan")
ax.legend()

plt.show()
