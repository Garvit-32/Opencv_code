import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('opencv-logo.png')
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# It is easier to draw and find contour in gray scale colour
ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)

# contours is a python list of all the contours in the image. Each individual contour is a numpy array of (x,y) coordinate 

contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("No. of contours = "+str(len(contours)))
# print(contours)
cv2.drawContours(img,contours,-1,(0,255,255),7)
cv2.imshow('image',img)
cv2.imshow('ImGray',imgray)
cv2.imshow('Gray',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()