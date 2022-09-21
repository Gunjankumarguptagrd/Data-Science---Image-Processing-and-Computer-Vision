# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 11:18:29 2022

@author: Gunjan
"""
#result Blending with Trackbars 

import numpy as np
import cv2 as cv 
#read two different images of same channel
img1 = cv.imread("D:\DATA Science 360 DigiTMG\AI\Gunjan.png")
img1 = cv.resize(img1,(500,700))
img2 = cv.imread("D:\DATA Science 360 DigiTMG\AI\loin.jpg")
img2 = cv.resize(img2,(500,700))
    
def blend(x):
    pass

img = np.zeros((400,400,3),np.uint8)
cv.namedWindow('win') #create track bar windows
cv.createTrackbar('alpha','win',1,100,blend)
switch = '0 : OFF \n 1 : ON'  #create switch for invoke the trackbars
cv.createTrackbar(switch,'win',0,1,blend)  #create track bar for switch
while(1):
    alpha = cv.getTrackbarPos('alpha','win')
   
    s = cv.getTrackbarPos(switch,'win')
    na = float(alpha/100)
    
    if s == 0:
        dst = img[:]
    else:
        dst = cv.addWeighted(img1,1-na,img2,na,0)
        cv.putText(dst, str(alpha), (20, 50), cv.FONT_ITALIC,
                   2, (0, 125, 255), 2)
    cv.imshow('dst',dst)

    k=cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
cv.waitKey(0)    

cv.destroyAllWindows()

"D:\DATA Science 360 DigiTMG\AI\loin.jpg"