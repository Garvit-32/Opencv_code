import cv2

# cv2.IMREAD_COLOR 1 Loads a color image.
# cv2.IMREAD_GRAYSCALE 0 Loads image in grayscale mode
# cv2.IMREAD_UNCHANGED -1 Loads image as such including alpha channel



img = cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
  cv2.destroyAllWindows()
elif k == ord('s'):
  cv2.imwrite('lena_copy.png', img)
  cv2.destroyAllWindows()