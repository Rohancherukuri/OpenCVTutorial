# Drawing lines and shapes on the webcam in python using open-cv
import cv2
import numpy as np
import time
from os import system

def main():
    """This is a main function"""
    cam = cv2.VideoCapture(0)
    cam.set(3,640) # Setting width
    cam.set(4,480) # Setting height
    print("Opening the webcam...")
    while cam.isOpened():
        _,frame = cam.read()
        width = int(cam.get(3)) # Getting the width of the frame
        height = int(cam.get(4)) # Getting the height of the frame
        # img = cv2.line(frame,(0,0),(width,height),(255,0,0),10)
        # img = cv2.line(img,(0,height),(width,0),(0,255,0),10)
        # img = cv2.rectangle(frame,(100,50),(300,220),(128,128,128),10)
        # img = cv2.circle(frame,(300,300),60,(0,0,255),-1)
        font = cv2.FONT_HERSHEY_COMPLEX
        img = cv2.putText(frame, "Welcome Rohan!", (60,height - 20), font,2,(0,255,0),5,cv2.LINE_AA)
        cv2.imshow("webcam",img)
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
        print("Error occurred: "+str(e))
    finally:
        t3 = t2 - t1
        print("[Finished in: "+str(round(t3,3))+" sec]")