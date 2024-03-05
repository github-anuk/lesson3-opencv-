import cv2

image=cv2.imread("pfp.jpg")
cv2.imshow("og",image)

#h = hue , s = staturation v = value

GrayImage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("gray image",GrayImage)
cv2.waitKey(0)
cv2.destroyAllWindows