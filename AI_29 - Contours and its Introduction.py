# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 00:15:10 2022

@author: Gunjan
"""

#Contours - 
#Contours can be explained simply as a curve joining all the continuous points 
#(along the boundary), having same color or intensity. 

#The contours are a useful tool for shape analysis and object detection and recognition

#For better accuracy, use binary images and also apply edge detection before 
#finding countours.

#findCountour function manipulate original imge so copy it before proceeding.
#findContour is like finding white object from black background.
#so you must turn image in white and background is black.

#We have to find and draw contours as per the requirement.

import cv2
import numpy as np
img = cv2.imread("Data\\logo.jpg")
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(img1,127,255,0)
#findcontour(img,contour_retrival_mode,method)
cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#Here cnts is a list of contours. ANd each contour is an array with x, y cordinate   
#hier variable called hierarchy and it contain image information.
print("Number of contour==",cnts,"\ntotal contour==",len(cnts))
print("Hierarchy==\n",hier)

#drawcontour(img,cnts,id of contour,color,thickness)#here if we draw all
#contour just pass -1
#Draw the contours
img = cv2.drawContours(img,cnts,-1,(176,10,15),4)


#ouput----
cv2.imshow("original===",img)
cv2.imshow("gray==",img1)
cv2.imshow("thresh==",thresh)
cv2.waitKey(0)
cv2.destroyAllwindow()

#-------------- Self Study---------------#

import numpy as np
import cv2

img = cv2.imread("D:\DATA Science 360 DigiTMG\AI\logo.jpg")
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thres = cv2.threshold(img1, 20,255,0)

#findCounters (img,counter_retrival_mode, method)
cnts,hier = cv2.findContours(thres,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(cnts,len(cnts))

#Draw the contours
img = cv2.drawContours(img,cnts,-1,(16,100,115),4)


cv2.imshow("logo === ", img)
cv2.imshow("Gray === ", img1)
cv2.imshow("thres === ", thres)

cv2.waitKey(0)
cv2.destroyAllwindow()