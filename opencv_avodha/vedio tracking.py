import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while(1):
    _,frame=cap.read()
    cv2.imshow('original', frame)
    #rgb format image converts into hsv
    new_image=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV conversion',new_image)

    # store lower and upper bound of blue color in array
    lower_bound=np.array([110, 50, 50])
    upper_bound=np.array([130, 252, 252])
    # image provide this bound and only select that image
    mask=cv2.inRange(new_image,lower_bound,upper_bound)
    cv2.imshow('red only',mask)

    # display the selected image color
    result=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('track',result)

    # finding exact color of red
    # red_rgb=np.uint8([[[255,0,0]]])
    # red_hsv=cv2.cvtColor(red_rgb,cv2.COLOR_BGR2HSV)
    # print(red_hsv)
    if cv2.waitKey(10000) & 0xFF==27 :
        break
cv2.destroyAllWindows()