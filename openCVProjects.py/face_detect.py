import cv2 as cv

def rescaleFrame(Frame,scale=3):
    # Usefule for images,video,live video
    width=int(Frame.shape[1]*scale)
    height=int(Frame.shape[0]*scale)
    dimension=(width,height)
    return cv.resize(Frame,dimension,interpolation=1)


img=cv.imread("F:\ML projects_py/animalimages\oscar-sutton-yihlaRCCvd4-unsplash.jpg")
img=rescaleFrame(img)
# cv.imshow("img",img)



gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

haar_cascade=cv.CascadeClassifier('F:\ML projects_py\openCVProjects.py\haar_face.xml')
faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=3)
print("Number of face found : ",len(faces_rect))
for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow("detected face",img)

cv.waitKey(0)