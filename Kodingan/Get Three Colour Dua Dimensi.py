from colorthief import ColorThief
import matplotlib.pyplot as plt

# Daftar file gambar
image_files = ["Mask group.png", "Mask group 2.png", "Mask group 3.png"]

# Fungsi untuk mendapatkan warna dominan
def get_dominant_color(image_file):
    ct = ColorThief(image_file)
    return ct.get_color(quality=1)

# Ambil warna dominan dari masing-masing gambar
dominant_colors = [get_dominant_color(image) for image in image_files]

# Hitung rata-rata RGB untuk setiap gambar
average_colors = [sum(color) / 3 for color in dominant_colors]

# Tampilkan nilai warna dan rata-rata
for i, (color, avg) in enumerate(zip(dominant_colors, average_colors)):
    hex_color = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
    print(f"Gambar {i+1} - Dominan RGB: {color}, HEX: {hex_color}, Rata-rata: {avg:.2f}")

# Plot dalam grafik 2D
plt.figure(figsize=(8, 6))

# Plot rata-rata warna untuk setiap gambar
for i, (avg, color) in enumerate(zip(average_colors, dominant_colors)):
    plt.scatter(i + 1, avg, color=f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}", s=100, label=f"Gambar {i+1}")
    plt.text(i + 1, avg, f"Gambar {i+1}", fontsize=10, ha='right')

# Atur sumbu dan judul
plt.xlabel("Gambar")
plt.ylabel("Rata-rata RGB")
plt.title("Perbandingan Rata-rata Warna Dominan")
plt.xticks(range(1, len(image_files) + 1), [f"Gambar {i+1}" for i in range(len(image_files))])
plt.legend()
plt.grid(True)

plt.show()
