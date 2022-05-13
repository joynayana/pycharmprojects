import cv2
img=cv2.imread('dog.jpg',1)

cv2.line(img,(0,0),(200,200),(255,0,0),5)
cv2.rectangle(img,(0,0),(200,200),(60, 179, 113),5)
cv2.circle(img,(100,100),50,(238, 130, 238),-1)
font=cv2.FONT_HERSHEY_SIMPLEX
fontColor=(106, 90, 205)
lineType=cv2.LINE_AA
cv2.putText(img,"Hello",(1,270),font,2,fontColor,lineType,2)
cv2.imshow('dog with shapes',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
