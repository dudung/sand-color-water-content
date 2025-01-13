from colorthief import ColorThief
import matplotlib.pyplot as plt

# File gambar
image_file = "Mask group 3.png"

# Ambil warna paling dominan
ct = ColorThief(image_file)
dominant_color = ct.get_color(quality=1)  # quality=1 untuk hasil yang lebih akurat

# Konversi warna ke format HEX
hex_color = f"#{dominant_color[0]:02x}{dominant_color[1]:02x}{dominant_color[2]:02x}"

# Tampilkan warna dominan
print(f"Warna dominan (RGB): {dominant_color}")
print(f"Warna dominan (HEX): {hex_color}")

# Visualisasikan warna dominan
plt.figure(figsize=(2, 2))
plt.imshow([[dominant_color]])
plt.axis('off')
plt.title(f"Dominant Color: {hex_color}")
plt.show()
