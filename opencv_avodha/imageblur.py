import cv2
import numpy as np
img=cv2.imread('dog.jpg',1)
#find average of image placing in 5by 5 matrix
matrix=np.ones((5,5),np.float32)/25
# blur image
new_img=cv2.filter2D(img,-1,matrix)
cv2.imshow('old',img)
cv2.imshow('new',new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()