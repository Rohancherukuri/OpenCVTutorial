# Colors and color detection using open-cv in python
import cv2
import numpy as np
import time
from os import system

def main():
    """This is a main function"""
    cam = cv2.VideoCapture(0)
    cam.set(3,640) # Setting width of the frame
    cam.set(4,480) # Setting height of the frame
    print("Opening the webcam...")
    while cam.isOpened():
        _,frame = cam.read()
        width = int(cam.get(3))
        height = int(cam.get(4))
        # BGR_color = np.array([[[255,0,0]]])
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # Converts from BGR color scheme to HSV
        lower_blue = np.array([90,50,50])
        upper_blue = np.array([130,255,255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        result = cv2.bitwise_and(frame,frame,mask = mask)
        cv2.imshow("Masked Webcam",mask)
        cv2.imshow("Webcam",result)
        if cv2.waitKey(1) == ord("q"):
            print("Closing the webcam...")
            time.sleep(0.5)
            system("clear")
            break
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        t1 = time.perf_counter()
        main()
        t2 = time.perf_counter()
    except Exception as e:
        print("Error occured: "+str(e))
    finally:
        t3 = t2 - t1
        print("[Finished in: "+str(round(t3,3))+" sec]")