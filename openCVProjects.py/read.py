import cv2 as cv
import numpy as np

# image_reading
# img=cv.imread('F:\ML projects_py/animalimages\cat.jpg')
# cv.imshow("cat",img)

# video_capturing
# capture=cv.VideoCapture(0)
# while True:
#     isTrue,frame=capture.read()
#     cv.imshow("video",frame)
#     if(cv.waitKey(2)&0xFF==ord('d')):
#         break

# rescaling the frames
def ChangeRes(width,height):
    #usefule only for live video
    capture.set(3,width)
    capture.set(4,height)

capture=cv.VideoCapture(0)
while True:
    isTrue,frame=capture.read()
    cv.imshow("video",frame)

capture=cv.VideoCapture(0)
ChangeRes(480,320)
cv.imshow("captur",capture)


# def rescaleFrame(Frame,scale=0.25):
#     # Usefule for images,video,live video
#     width=int(Frame.shape[1]*scale)
#     height=int(Frame.shape[0]*scale)
#     dimension=(width,height)
#     return cv.resize(Frame,dimension,interpolation=cv.INTER_AREA)

# # image_reading
# img=cv.imread('F:\ML projects_py/animalimages\cat.jpg')
# modified=rescaleFrame(img,scale=0.2)
# cv.imshow("cat",img)
# cv.imshow("modified",modified)


# # cv.rectangle(blank,(0,0),(200,230),)
cv.waitKey(0)
