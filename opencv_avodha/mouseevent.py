import cv2
def draw_circle(event, x, y, flag, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(255, 0, 0),-1)

img = cv2.imread('dog.jpg', 1)
cv2.namedWindow("dog")
cv2.setMouseCallback('dog',draw_circle)
while(1):
    cv2.imshow('dog',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()