from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys

# Fungsi untuk menghitung luminansi
def calculate_luminance(color):
    r, g, b = [c / 255.0 for c in color]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

# Fungsi untuk memproses gambar dan menghasilkan palet warna yang terurut
def process_image(image_path, color_count=10):
    ct = ColorThief(image_path)
    palette = ct.get_palette(color_count=color_count)
    sorted_palette = sorted(palette, key=calculate_luminance)
    return sorted_palette

# Memproses dua gambar
image1_path = "PaletteT5_1.jpg"
image2_path = "TestPT2_2.jpg"

palette1 = process_image(image1_path)
palette2 = process_image(image2_path)

# Fungsi untuk menampilkan palet dan grafik luminansi
def display_palette_and_luminance(palette, title, ax_palette, ax_luminance):
    luminance = [calculate_luminance(color) for color in palette]

    # Tampilkan palet warna
    ax_palette.imshow([[palette[i] for i in range(len(palette))]])
    ax_palette.set_title(f"{title} - Palette")
    ax_palette.axis('off')

    # Tampilkan grafik luminansi
    ax_luminance.bar(range(len(luminance)), luminance, color=[tuple(c / 255.0 for c in color) for color in palette])
    ax_luminance.set_title(f"{title} - Luminance")
    ax_luminance.set_xlabel("Color Index")
    ax_luminance.set_ylabel("Luminance")
    ax_luminance.set_ylim(0, 1)

# Plot palet warna dan grafik luminansi untuk kedua gambar
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Gambar pertama
display_palette_and_luminance(palette1, "Pasir Terang", axs[0, 0], axs[0, 1])

# Gambar kedua
display_palette_and_luminance(palette2, "Pasir Gelap", axs[1, 0], axs[1, 1])

plt.tight_layout()
plt.show()
