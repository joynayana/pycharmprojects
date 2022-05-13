import cv2
import numpy as np
img=cv2.imread('dog.jpg',1)
new_img=cv2.blur(img,(5,5))
gaussian_blur=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('old',img)
cv2.imshow('blur',new_img)
cv2.imshow('guassia',gaussian_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()