import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

print(cap.isOpened())
while(cap.isOpened()):
    # ret store true or false it is true when frame is available


#     Python: cv.CAP_PROP_FRAME_WIDTH: Width of the frames in the video stream.
#     Python: cv.CAP_PROP_FRAME_HEIGHT: Height of the frames in the video stream.
#     Color image loaded by OpenCV is in BGR mode. But Matplotlib displays in RGB mode.

    ret, frame = cap.read()
    # print(ret)
    if ret == True:
       print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
       print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

       out.write(frame)

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       cv2.imshow('frame', gray)

       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()