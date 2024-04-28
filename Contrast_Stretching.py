import cv2
import numpy as np

# Baca gambar
image = cv2.imread('exm.tif')

# Konversi gambar ke grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Hitung nilai minimum dan maksimum intensitas piksel
min_intensity = np.min(grayscale_image)
max_intensity = np.max(grayscale_image)

# Tentukan rentang yang baru
new_min_intensity = 0
new_max_intensity = 255

# Lakukan contrast stretching
stretched_image = ((grayscale_image - min_intensity) / (max_intensity - min_intensity)) * (new_max_intensity - new_min_intensity) + new_min_intensity

# Konversi ke dalam format yang sesuai
stretched_image = np.uint8(stretched_image)

# Tampilkan gambar asli dan gambar yang telah di-stretching kontrasnya
cv2.imshow('Original Image', grayscale_image)
cv2.imshow('Contrast Stretched Image', stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
