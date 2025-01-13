from colorthief import ColorThief
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Daftar file gambar
image_files = [f"W{i}.png" for i in range(0, 18)]

# Fungsi untuk mendapatkan warna dominan
def get_dominant_color(image_file):
    ct = ColorThief(image_file)
    return ct.get_color(quality=1)

# Ambil warna dominan dari masing-masing gambar
dominant_colors = [get_dominant_color(image) for image in image_files]

# Cek apakah ada warna timpang tindih/sama
color_map = {}
duplicates = []

for i, color in enumerate(dominant_colors):
    if color in color_map:
        duplicates.append((color_map[color], i + 1))  # Simpan pasangan gambar yang memiliki warna sama
    else:
        color_map[color] = i + 1

# Tampilkan informasi warna
print("Informasi Warna Dominan:")
for i, color in enumerate(dominant_colors):
    hex_color = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
    print(f"Gambar {i+1} - Dominan RGB: {color}, HEX: {hex_color}")

# Tampilkan hasil duplikasi (jika ada)
if duplicates:
    print("\nGambar-gambar dengan warna dominan yang sama:")
    for dup1, dup2 in duplicates:
        print(f"- Gambar {dup1} dan Gambar {dup2} memiliki warna dominan yang sama.")
else:
    print("\nTidak ada gambar dengan warna dominan yang sama.")

# Terapkan PCA untuk mengurangi dimensi dari RGB (3D) ke 2D
pca = PCA(n_components=2)
reduced_colors = pca.fit_transform(dominant_colors)

# Plot hasil reduksi dimensi
plt.figure(figsize=(10, 8))
for i, (reduced, original) in enumerate(zip(reduced_colors, dominant_colors)):
    x, y = reduced
    plt.scatter(x, y, color=f"#{original[0]:02x}{original[1]:02x}{original[2]:02x}", s=150, label=f"W{i}")
    plt.text(x, y, f"W{i}", fontsize=10, color="black")

# Atur label dan judul grafik
plt.xlabel("Dominasi Warna Utama")
plt.ylabel("Variasi Warna Sekunder")
plt.title("Perbandingan Warna pada Pasir Terang Dominan Setelah Reduksi Dimensi dengan PCA")
plt.legend()
plt.grid(True)
plt.show()
