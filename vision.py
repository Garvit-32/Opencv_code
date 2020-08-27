import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('messi5.jpg',0)


titles = ['image']
image = [img]

for i in range(1):
    plt.subplot(1,1,i+1)
    plt.imshow(image[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
