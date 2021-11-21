import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow("blank",blank)
# blank[200:300,300:500]=0,25,50
# cv.imshow("color",blank)

# 2.draw a rectagle
# cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(0,0,250),thickness=-1)
# cv.imshow("rectangle",blank)

# Draw circle
# cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),90,(0,0,234),thickness=-1)
# cv.imshow("circle",blank)

# write text on images
cv.putText(blank,"hello i`m kiran here!!",(blank.shape[0]//6,blank.shape[1]//2),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,237,0),2)
cv.imshow("line",blank)
cv.waitKey(0)