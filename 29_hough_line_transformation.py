import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sudoku.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize=3)
lines = cv2.HoughLines(edges,1,np.pi/180,200)
# cv2.HoughLines(image,rho,theta,threshold,line)
# print(lines)
for line in lines:
    rho,theta = line[0]
    # print(rho)
    # print(theta)
    a = np.cos(theta)
    # print(a)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    # x1 stores the rounded off value for it (r*cos(theta)-1000*sin(theta))
    x1 = int(x0 + 1000*(-b))
    # y1 stores the rounded off value for it (r*sin(theta)+1000*cos(theta))
    y1 = int(y0 + 1000*(a))
    # x2 stores the rounded off value for it (r*cos(theta)+1000*sin(theta))
    x2 = int(x0 - 1000*(-b))
    # y2 stores the rounded off value for it (r*sin(theta)-1000*cos(theta))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

# rho : distance resolution of the accumulator in the pixel
# theta : angle resolution of the accumulator in radian
# line : Output vector line 

cv2.imshow('image',img)
cv2.imshow('canny',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()