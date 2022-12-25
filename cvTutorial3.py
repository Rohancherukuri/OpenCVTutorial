# Using some basic functions in opencv in python
import cv2
import numpy as np
IMG_PATH = "/home/rohanoxob/My2DGame/traveler.png"
kernel = np.ones((5,5),np.uint8)
img = cv2.imread(IMG_PATH)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,100,100)
imgDilation = cv2.dilate(imgCanny,kernel,iterations = 1)
imgEroded = cv2.erode(imgDilation,kernel,iterations = 1)

cv2.imshow("GreyImage",imgGray)
cv2.imshow("BlurImage",imgBlur)
cv2.imshow("CannyImage",imgCanny)
cv2.imshow("DilationImage",imgDilation)
cv2.imshow("ErodedImage",imgEroded)
cv2.waitKey(0)
cv2.destroyAllWindows()