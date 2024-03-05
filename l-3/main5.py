import cv2

image=cv2.imread("pfp.jpg")

t_lower = 50
t_upper =250

edge=cv2.Canny(image,t_lower,t_upper)
cv2.imshow("og",image)
cv2.imshow("edge",edge)

cv2.waitKey(0)
cv2.destroyAllWindows()