# reshaping and resizeing image in opencv in python
import cv2
IMG_PATH = "/home/rohanoxob/My2DGame/traveler.png"
img = cv2.imread(IMG_PATH)
print(img.shape)
imgResized = cv2.resize(img,(100,200))
imgCropped = img[0:50,50:100]
cv2.imshow("Original Image",img)
cv2.imshow("Resized Image",imgResized)
cv2.imshow("Cropped Image",imgCropped)
cv2.waitKey(0)