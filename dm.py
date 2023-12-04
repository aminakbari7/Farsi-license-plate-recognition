import cv2
import imutils as i
image1=cv2.imread("1.jpg")
image2=i.resize(image1,width=400)
print(image1==image2)