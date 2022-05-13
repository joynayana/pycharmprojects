import cv2
img=cv2.imread('images.jpg',0)
ret,thresh=cv2.threshold(img,60,255,cv2.THRESH_BINARY)
cv2.imshow('real',img)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()