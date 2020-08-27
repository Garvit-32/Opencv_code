# img.shape returns a tuple of number of rows, columns, and channels
# img.size returns Total number of pixels is accessed
# img.dtype returns Image datatype is obtained
# cv2.split(img) - output vector of arrays; the arrays themselves are reallocated, if needed.
# cv2.merge((b,g,r)) - The number of channels will be the total number of channels in the matrix array.
# cv2.resize - resize the image
# dst = cv2.add(img, img2) - Calculates the per-element sum of two arrays or an array and a scalar.
# dst = cv2.addWeighted(img, .2, img2, .8, 0) - Calculates the weighted sum of two arrays.

import cv2
import numpy as np


img = cv2.imread('messi5.jpg',)
img2 = cv2.imread('opencv-logo.png')

print(img.size)
print(img.shape)
print(img.dtype)

b,g,r = cv2.split(img)
# print(b)
img = cv2.merge((b,g,r))
# [width,height]
ball = img[280:340,330:390]
img[273:333,100:160] = ball

img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))
# size of the image added must be same 
# dst = cv2.add(img,img2)
dst = cv2.addWeighted(img,.9,img2,0.1,0)


cv2.imshow('image',img)
cv2.imshow('Add',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()