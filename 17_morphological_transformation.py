import cv2
import numpy as np
from matplotlib import pyplot as plt

# morphological operation are some simple operations based on size of image


img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5,5), np.uint8)
# a kernal tell you how to change the value of the any given pixel by combining it with different amounts of the neighbouring pixel
dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=1)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
# opening is erosion followed by dialation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)
# closing is dialation followed by erosion
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
# mg is difference between dialation and erosion
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)
# th is difference between erosion and dilation

titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()