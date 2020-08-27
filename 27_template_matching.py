# Template Matching is a method for searching and finding the location of a template image in a larger image. OpenCV comes with a function cv.matchTemplate() for this purpose.


import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
template = cv2.imread('messi_face.jpg',0)


w,h = template.shape[::-1]
# print(template.shape)

res = cv2.matchTemplate(grey_img,template,cv2.TM_CCOEFF_NORMED)
# print(res)
threshold = 0.9
loc = np.where(res >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,0,255),2)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()