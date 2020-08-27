import cv2
import numpy as np

img = cv2.imread('road.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150)
cv2.imshow('edges',edges)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)

# minLineLength : Minimum length of line. Line segment shorter than this are rejected
# maxLineGap : Max allowed gap between line segments to retreat them as a single line

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()