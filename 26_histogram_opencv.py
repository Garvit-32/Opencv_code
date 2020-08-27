# A Histogram is a variation of a bar chart in which data values are grouped together and put into different classes.
# This grouping allows you see how frequently data in each class occur in the data set. 

import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('lena.jpg',0)
# img = np.zeros((200,200),np.uint8)
# cv2.rectangle(img,(0,100),(200,200),(255),-1)
# cv2.rectangle(img,(0,50),(100,100),(127),-1)
# b,g,r = cv2.split(img)
# cv2.imshow("img",img)
# cv2.imshow("b",b)
# cv2.imshow("g",g)
# cv2.imshow("r",r)
# # plt.hist(img.ravel(),256,[0,256])
# plt.hist(b.ravel(),256,[0,256])
# plt.hist(g.ravel(),256,[0,256])
# plt.hist(r.ravel(),256,[0,256])

hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()