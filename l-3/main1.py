import cv2

image=cv2.imread("pfp.jpg")

#h = hue , s = staturation v = value

hsvImage=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

cv2.imshow("hsv image",hsvImage)
cv2.waitKey(0)
cv2.destroyAllWindows