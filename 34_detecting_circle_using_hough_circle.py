import cv2
import numpy as np

img = cv2.imread('smarties.png')
output = img.copy()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Hough circle method is work better with blur method

gray = cv2.medianBlur(gray,5)
circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

detected_circles = np.uint16(np.around(circles))
for (x,y,r) in detected_circles[0,:]:
    cv2.circle(output,(x,y),r,(255,255,50),3)
    cv2.circle(output,(x,y),2,(0,255,255),3)


# dp : Inverse ratio of the accumulator resolution to the image resolution
# minDist : Minimum distance between the center of the detected circle 



cv2.imshow('output',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
