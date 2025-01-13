from colorthief import ColorThief
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Daftar file gambar untuk pasir gelap dan terang
dark_sand_files = [f"W{i}_gelap.png" for i in range(0, 18)]
light_sand_files = [f"W{i}.png" for i in range(0, 18)]

# Fungsi untuk mendapatkan warna dominan
def get_dominant_color(image_file):
    ct = ColorThief(image_file)
    return ct.get_color(quality=1)

# Ambil warna dominan dari masing-masing gambar
dark_colors = [get_dominant_color(image) for image in dark_sand_files]
light_colors = [get_dominant_color(image) for image in light_sand_files]

# Gabungkan warna untuk PCA
all_colors = dark_colors + light_colors

# Terapkan PCA untuk mengurangi dimensi dari RGB (3D) ke 2D
pca = PCA(n_components=2)
reduced_colors = pca.fit_transform(all_colors)

# Pisahkan hasil reduksi untuk pasir gelap dan terang
dark_reduced = reduced_colors[:len(dark_colors)]
light_reduced = reduced_colors[len(dark_colors):]

# Plot hasil reduksi dimensi
fig, ax = plt.subplots(figsize=(14, 8))

# Plot untuk pasir gelap
dark_handles = []  # Simpan untuk legenda pasir gelap
for i, (reduced, original) in enumerate(zip(dark_reduced, dark_colors)):
    x, y = reduced
    point = ax.scatter(x, y, color=f"#{original[0]:02x}{original[1]:02x}{original[2]:02x}", s=150, label=f"Gelap W{i}")
    dark_handles.append(point)  # Tambahkan ke legenda
    ax.text(x, y, f"W{i}", fontsize=9, color="red")

# Plot untuk pasir terang
light_handles = []  # Simpan untuk legenda pasir terang
for i, (reduced, original) in enumerate(zip(light_reduced, light_colors)):
    x, y = reduced
    point = ax.scatter(x, y, color=f"#{original[0]:02x}{original[1]:02x}{original[2]:02x}", s=150, label=f"Terang W{i}", marker="^")
    light_handles.append(point)  # Tambahkan ke legenda
    ax.text(x, y, f"W{i}", fontsize=9, color="blue")

# Atur label dan judul grafik
ax.set_xlabel("Dominasi Warna Utama")
ax.set_ylabel("Variasi Warna Sekunder")
ax.set_title("Perbandingan Warna Dominan Pasir Gelap dan Pasir Terang")

# Tambahkan legenda untuk pasir gelap di kiri atas grafik
legend1 = ax.legend(handles=dark_handles, title="Pasir Gelap", loc="upper left",bbox_to_anchor=(1, 1), fontsize=9)
for label in legend1.get_texts():
    label.set_color('red')  # Ubah warna teks menjadi merah untuk legenda Pasir Gelap
ax.add_artist(legend1)  # Pastikan legenda ini tetap ada

# Tambahkan legenda untuk pasir terang di luar grafik
legend2 = ax.legend(handles=light_handles, title="Pasir Terang", loc="upper left", bbox_to_anchor=(1.12, 1), fontsize=9)
for label in legend2.get_texts():
    label.set_color('blue')  # Ubah warna teks menjadi merah untuk legenda Pasir Gelap

plt.grid(True)
plt.tight_layout()
plt.show()
