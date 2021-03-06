import os

import numpy as np
import cv2

im = cv2.imread('a.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)


contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(im,contours,-1,(0,0,255),3)

cv2.imshow("img", im)
cv2.waitKey(0)

