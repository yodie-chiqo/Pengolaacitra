import cv2
import numpy as np

# Baca gambar
image = cv2.imread('exm.tif')

# Tentukan kernel filter blur
kernel_size = 2  # Ukuran kernel
kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)  # Kernel filter rata-rata

# Terapkan operasi konvolusi
blurred_image = cv2.filter2D(image, -5, kernel)

# Tampilkan gambar asli dan gambar yang telah diberi filter blur
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
