import cv2

def click_event(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x)+','+str(y)
        cv2.putText(img,text,(x,y),font,1,(0,255,255),3)
        cv2.imshow('image',img)

img = cv2.imread('messi5.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()