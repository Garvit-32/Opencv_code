import cv2
import numpy as np
import matplotlib.pyplot as plt


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.1,4)
# print(faces)
# scaleFactor = Parameter specifying how much the image size is reduced at each image scale.
# minNeighbours = Parameter specifying how many neighbours each candidate rectangle should have to retain it
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows(0)