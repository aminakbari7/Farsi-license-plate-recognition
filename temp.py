import imutils
import cv2
a1=cv2.imread("1.jpg")
a2=cv2.imread("1.jpg")
a2=imutils.resize(a2, width=700)
a3=cv2.imread("3.jpg")
print(a1==a2)
cv2.imshow("name",a2)
cv2.waitKey(0)