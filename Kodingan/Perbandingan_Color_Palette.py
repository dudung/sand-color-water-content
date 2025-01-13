from colorthief import ColorThief
import matplotlib.pyplot as plt

# Daftar file gambar pasir gelap dan terang
image_files_gelap = [f"W{i}_gelap.png" for i in range(0, 18)]
image_files_terang = [f"W{i}.png" for i in range(0, 18)]  # Misalnya gambar pasir terang

# Fungsi untuk mendapatkan warna dominan
def get_dominant_color(image_file):
    ct = ColorThief(image_file)
    return ct.get_color(quality=1)

# Hitung intensitas warna untuk mengurutkan dari gelap ke terang
def calculate_intensity(color):
    r, g, b = color
    return 0.299 * r + 0.587 * g + 0.114 * b

# Ambil warna dominan dari masing-masing gambar
dominant_colors_gelap = [get_dominant_color(image) for image in image_files_gelap]
dominant_colors_terang = [get_dominant_color(image) for image in image_files_terang]

# Urutkan warna berdasarkan intensitas
sorted_colors_gelap = sorted(dominant_colors_gelap, key=calculate_intensity)
sorted_colors_terang = sorted(dominant_colors_terang, key=calculate_intensity)

# Tentukan ukuran grid (jumlah baris dan kolom)
num_columns = 5
num_rows = (len(sorted_colors_gelap) + num_columns - 1) // num_columns  # Hitung jumlah baris

# Buat palet warna dengan grid untuk pasir gelap dan terang
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 10))

# Pasir Gelap
for i, color in enumerate(sorted_colors_gelap):
    r, g, b = color
    hex_color = f"#{r:02x}{g:02x}{b:02x}"
    
    # Tentukan posisi kotak dalam grid (baris dan kolom)
    row = i // num_columns
    col = i % num_columns
    
    # Tambahkan kotak ke plot Pasir Gelap
    ax1.add_patch(plt.Rectangle((col, num_rows - row - 1), 1, 1, color=hex_color))
    
    # Tambahkan teks dengan warna putih
    ax1.text(col + 0.5, num_rows - row - 1 + 0.5, hex_color, ha='center', va='center', fontsize=8, color='white', rotation=45)

# Pasir Terang
for i, color in enumerate(sorted_colors_terang):
    r, g, b = color
    hex_color = f"#{r:02x}{g:02x}{b:02x}"
    
    # Tentukan posisi kotak dalam grid (baris dan kolom)
    row = i // num_columns
    col = i % num_columns
    
    # Tambahkan kotak ke plot Pasir Terang
    ax2.add_patch(plt.Rectangle((col, num_rows - row - 1), 1, 1, color=hex_color))
    
    # Tambahkan teks dengan warna putih
    ax2.text(col + 0.5, num_rows - row - 1 + 0.5, hex_color, ha='center', va='center', fontsize=8, color='white', rotation=45)

# Atur tampilan
ax1.set_xlim(0, num_columns)
ax1.set_ylim(0, num_rows)
ax1.axis("off")
ax1.set_title("Color Palette Pasir Gelap (Gelap ke Terang)")

ax2.set_xlim(0, num_columns)
ax2.set_ylim(0, num_rows)
ax2.axis("off")
ax2.set_title("Color Palette Pasir Terang (Gelap ke Terang)")

plt.tight_layout()
plt.show()

# Tampilkan informasi warna setelah diurutkan
print("Warna dominan Pasir Gelap yang telah diurutkan (gelap ke terang):")
for i, color in enumerate(sorted_colors_gelap):
    hex_color = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
    print(f"{i + 1}. RGB: {color}, HEX: {hex_color}")

print("\nWarna dominan Pasir Terang yang telah diurutkan (gelap ke terang):")
for i, color in enumerate(sorted_colors_terang):
    hex_color = f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"
    print(f"{i + 1}. RGB: {color}, HEX: {hex_color}")
