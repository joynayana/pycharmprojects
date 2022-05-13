import cv2
img=cv2.imread('dog.jpg')
# print(img) showing pixel value
cv2.imshow('dog',img)
cv2.waitKey(10000)
# cv2.imwrite('newdog.png',img)
cv2.destroyAllWindows()
