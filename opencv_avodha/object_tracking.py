import cv2
import numpy as np
#read a image and display it
img=cv2.imread('circle.png',1)
cv2.imshow('original',img)

#rgb format image converts into hsv
new_image=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV conversion',new_image)

# store lower and upper bound of red color in array
lower_bound=np.array([169, 100, 100])
upper_bound=np.array([189, 255, 255])
# image provide this bound and only select that image
mask=cv2.inRange(new_image,lower_bound,upper_bound)
cv2.imshow('red only',mask)

# display the selected image color
result=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('track',result)

# finding exact color of red
red_rgb=np.uint8([[[255,0,0]]])
red_hsv=cv2.cvtColor(red_rgb,cv2.COLOR_BGR2HSV)
print(red_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()