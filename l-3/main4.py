import cv2

image=cv2.imread("pfp.jpg")
 
(rows, cols ) = image.shape[0:2]

M = cv2.getRotationMatrix2D((cols/2 , rows / 2),180,1)

res = cv2.warpAffine(image, M,(cols,rows))

cv2.imshow("roate",res)
cv2.waitKey(0)
cv2.destroyAllWindows()