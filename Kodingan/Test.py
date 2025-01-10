from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys

ct = ColorThief("PaletteT5_1.jpg")
a = ct.get_palette(color_count=10)

plt.imshow([[a[i] for i in range(5)]])
plt.show()

for color in a:
    print(color)
    print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}")
    print(colorsys.rgb_to_hsv(*color))
    print(colorsys.rgb_to_hls(*color))