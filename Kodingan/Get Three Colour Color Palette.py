from colorthief import ColorThief
import matplotlib.pyplot as plt

# Daftar file gambar
image_files = [f"W{i}_gelap.png" for i in range(0, 18)]

# Fungsi untuk mendapatkan warna dominan
def get_dominant_color(image_file):
    ct = ColorThief(image_file)
    return ct.get_color(quality=1)

# Hitung intensitas warna untuk mengurutkan dari gelap ke terang
def calculate_intensity(color):
    r, g, b = color
    return 0.299 * r + 0.587 * g + 0.114 * b

# Ambil warna dominan dari masing-masing gambar
dominant_colors = [get_dominant_color(image) for image in image_files]

# Urutkan warna berdasarkan intensitas
sorted_colors = sorted(dominant_colors, key=calculate_intensity)

# Tentukan ukuran grid (jumlah baris dan kolom)
num_columns = 5
num_rows = (len(sorted_colors) + num_columns - 1) // num_columns  # Hitung jumlah baris

# Buat palet warna dengan grid
fig, ax = plt.subplots(figsize=(10, 10))

# Tambahkan kotak warna ke dalam grid
for i, color in enumerate(sorted_colors):
    r, g, b = color
    hex_color = f"#{r:02x}{g:02x}{b:02x}"
    
    # Tentukan posisi kotak dalam grid (baris dan kolom)
    row = i // num_columns
    col = i % num_columns
    
    # Tambahkan kotak ke plot
    ax.add_patch(plt.Rectangle((col, num_rows - row - 1), 1, 1, color=hex_color))
    
    # Tambahkan teks dengan warna putih
    ax.text(col + 0.5, num_rows - row - 1 + 0.5, hex_color, ha='center', va='center', fontsize=8, color='white', rotation=45)

ax.set_xlim(0, num_columns)
ax.set_ylim(0, num_rows)
ax.axis("off")
plt.title("Color Palette Pasir Gelap (Gelap ke Terang)")

plt.tight_layout()
plt.show()

# Tampilkan informasi warna setelah diurutkan
print("Warna dominan yang telah diurutkan (gelap ke terang):")
for i, color in enumerate(sorted_colors):
    hex_color = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
    print(f"{i + 1}. RGB: {color}, HEX: {hex_color}")