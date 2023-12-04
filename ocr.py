from turtle import width
import cv2
import imutils
# let go
image =cv2.imread("5.jpg")
image2 =cv2.imread("5.jpg")
image =imutils.resize(image, width=700)
image2 =imutils.resize(image2, width=700)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #black and white
filtered=cv2.GaussianBlur(gray,(5,5),0)
edg=cv2.Canny(filtered,10,100)
temp=edg
contours,hir=cv2.findContours(edg.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image,contours,-1,(0,255,0),1)
contours=sorted(contours,key=cv2.contourArea,reverse=True)
plate=False
for c in contours :
    primeter=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.02*primeter,True)
    if len(approx)==4:
        x,y,w,h=cv2.boundingRect(c)
        if 2.5<=(w/h) <=4.5:
             plate=True
             cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)            
    break        
if not plate:
    for c in contours :
     primeter=cv2.arcLength(c,True)
     approx=cv2.approxPolyDP(c,0.01*primeter,True)
     if len(approx)>=4:
         x,y,w,h=cv2.boundingRect(c)
         if 2.5<=(w/h) <=4.5 and 10000<=w*h<=15000:
             plate=True
             cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
             break
         
cv2.imshow("name",image)
cv2.imshow("edg",temp)
cv2.waitKey(0)
    