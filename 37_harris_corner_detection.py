import cv2
import numpy as np

img = cv2.imread('chessboard_image.png')
img = cv2.resize(img,(512,512))
cv2.imshow("image",img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cornerHarris take image as float32 datatype and gray image 
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

# blocksize = size of neighbourhood considered for corner detection
# ksize = parameter for Sobel derivative

dst = cv2.dilate(dst,None)

img[dst > 0.01 * dst.max()] = [0,0,255]

cv2.imshow('dst',img)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
    
