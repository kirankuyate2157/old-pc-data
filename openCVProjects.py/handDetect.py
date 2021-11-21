import cv2 as cv
import time
import os


widthCam,heightCam=640,480
cap=cv.VideoCapture(1)
cap.set(2,widthCam)
cap.set(4,heightCam)
while(True):
    success,img=cap.read()
    cv.imshow("Image",img)
    cv.waiykey(1)

    
