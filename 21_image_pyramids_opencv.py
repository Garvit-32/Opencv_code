import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')

# pyrDown method
# lr1 = cv2.pyrDown(img)
# lr2 = cv2.pyrDown(lr1)

# pyrUp method
# Information is loose in pyrup method
# hr2 = cv2.pyrUp()


# Gaussian Pyramid
# layer = img.copy()
# gp = [layer]
# for i in range(6):
#     layer = cv2.pyrDown(layer)
#     gp.append(layer)
#     cv2.imshow(str(i),layer)

# Laplacian Pyramid 
# A level in laplacian pyramid is formed by the difference between that level in Gaussian pyramid and extented version of its gaussian pyramid layer
layer = img.copy()
gp = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer) 
    gp.append(layer)

layer = gp[5]
cv2.imshow('Upper level Gaussian Pyramid',layer)
lp = [layer]

for i in range(5,0,-1):
    # print(i)
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),laplacian)

# cv2.imshow('Original Image',img)
# cv2.imshow('Pyramid1',lr1)
# cv2.imshow('Pyramid2',lr2)
# cv2.imshow('Pyramid21',hr2)


cv2.waitKey(0)
cv2.destroyAllWindows()