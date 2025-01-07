from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys
from openpyxl import Workbook

# Ambil palet warna dari gambar
ct = ColorThief("180420.jpg")
palette = ct.get_palette(color_count=5)

# Tampilkan warna dengan matplotlib
plt.imshow([[palette[i] for i in range(5)]])
plt.axis('off')  # Hilangkan sumbu
plt.show()

# Buat workbook Excel
wb = Workbook()
ws = wb.active
ws.title = "Color Palette"

# Tambahkan header ke Excel
headers = ["R", "G", "B", "HEX", "HSV", "HLS"]
ws.append(headers)

# Masukkan data warna ke Excel
for color in palette:
    r, g, b = color
    hex_color = f"#{r:02x}{g:02x}{b:02x}"
    hsv = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
    hls = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)

    # Tambahkan ke file Excel
    ws.append([
        r, g, b,
        hex_color,
        f"({hsv[0]:.2f}, {hsv[1]:.2f}, {hsv[2]:.2f})",
        f"({hls[0]:.2f}, {hls[1]:.2f}, {hls[2]:.2f})"
    ])

# Simpan file Excel
output_file = "color_palette.xlsx"
wb.save(output_file)
print(f"Data warna telah disimpan di {output_file}")
