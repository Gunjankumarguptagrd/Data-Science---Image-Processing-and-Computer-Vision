#In this Video, we talk about ROI(Region of Interest)
#this concept is use to find target portion from image like eyes on face.
import cv2
import numpy as np

#read image
img = cv2.imread("Data\\roi_opr.jpg")
img = cv2.resize(img,(800,800))

#Now extract  area of interest from an image

#now pass like [y1:y2,x1:x2]
roi = img[50:205,320:440]
#cv2.imshow("roi image==",roi)

#putting roi into any pixel values

img[50:205,431:551] = roi   #actual 441:561
img[50:205,552:672] = roi 
img[50:205,200:320] = roi
img[50:205,80:200] = roi

#changing y===
img[400:555,60:180] = roi
cv2.imshow("original image==",img)

#Now try to use one image data into another image

img1 = cv2.imread("H:\\Data\\ironman.jpg")
img1 = cv2.resize(img1,(900,600))
img1[1:156,560:680] = roi

cv2.imshow("ironman",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

##---------- Self Study --------- ##
import numpy as np
import cv2

img = cv2.imread("D:\DATA Science 360 DigiTMG\AI\Gunjan.png")

#ROI
# (x1,y1) ->(205,17) , (x2, y2) ->(282,118)
#(y1:y2),(x1:x2)
#y = 100, x = 75
roi = img[17:118, 205:282]

img[17:118, 280:357] = roi #after head
img[17:118, 355:432] = roi #after head

img[17:118, 130:207] = roi # brfore head
img[17:118, 55:132] = roi # brfore head


cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()









