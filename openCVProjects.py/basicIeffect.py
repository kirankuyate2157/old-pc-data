import cv2 as cv

def resizeimage(frame,scale=0.20):
    width=int(frame.shape[0]*scale)
    height=int(frame.shape[1]*scale)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

img=cv.imread('animalimages/cat.jpg')
img=resizeimage(img)
cv.imshow("cat",img)

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("GRAY",gray)

# # how to blur image
# blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
# cv.imshow("blur",blur)

# edges cascand
canny=cv.Canny(img,450,350)
cv.imshow("canny",canny)

# dailating the images
daileted=cv.dilate(canny,(3,3),iterations=2)
cv.imshow("dialeted",daileted)

# eroding
eroded=cv.erode(daileted,(3,3),iterations=1)
cv.imshow("erode",eroded)

# resize
resized=cv.resize(img,(255,255),interpolation=cv.INTER_CUBIC)
cv.imshow("resized",resized)

# cropped
cropped=img[50:200,200:400]
cv.imshow("cropped",cropped)



cv.waitKey(0)
