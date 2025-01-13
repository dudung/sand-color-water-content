from colorthief import ColorThief
from PIL import Image
import numpy as np
from scipy.spatial import KDTree

def extract_palette(image_path, color_count=5):
    """
    Ekstrak palet warna dari gambar menggunakan ColorThief.
    """
    ct = ColorThief(image_path)
    palette = ct.get_palette(color_count=color_count)
    return palette

def rgb_to_hex(rgb):
    """
    Konversi warna RGB ke format hex.
    """
    return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

def match_colors(image_path, palette):
    """
    Identifikasi warna pada gambar target dan mencocokkan ke warna palet.
    """
    img = Image.open(image_path).convert("RGB")
    img_array = np.array(img)

    # Buat KDTree untuk pencarian cepat warna palet terdekat
    tree = KDTree(palette)
    matched_colors = []

    for row in img_array:
        matched_row = []
        for pixel in row:
            _, index = tree.query(pixel)  # Cari warna palet terdekat
            matched_row.append(rgb_to_hex(palette[index]))  # Simpan hasil dalam format hex
        matched_colors.append(matched_row)
    
    return matched_colors

def main():
    # Path gambar palette dan target
    palette_image_path = "PaletteT5_1.jpg"
    target_image_path = "Mask group.png"

    # Ekstrak palet warna dari gambar palet
    palette = extract_palette(palette_image_path)
    print("Extracted Palette (HEX):", [rgb_to_hex(color) for color in palette])

    # Cocokkan warna gambar target dengan palet
    matched_colors = match_colors(target_image_path, palette)
    
    # Simpan hasil sebagai file teks
    output_file = "matched_colors.txt"
    with open(output_file, "w") as f:
        for row in matched_colors:
            f.write(" ".join(row) + "\n")
    
    print(f"Matched colors saved to {output_file}")

if __name__ == "__main__":
    main()
