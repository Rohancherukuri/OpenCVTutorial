# Splitting the frame into 4 video web cams using open-cv in python
import cv2
import numpy as np
import time
from os import system

def main():
    """This is a main function"""
    cam = cv2.VideoCapture(0)
    # cam.set(3,640) # Setting width
    # cam.set(4,480) # Setting height
    print("Opening the webcam...")
    while cam.isOpened():
        _,frame = cam.read()
        width = int(cam.get(3)) # Getting frame width value
        height = int(cam.get(4)) # Getting frame height value
        img = np.zeros(frame.shape,np.uint8)
        smaller_frame = cv2.resize(frame,(0,0),fx = 0.5,fy = 0.5)
        img[:height // 2,:width //2] = cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180) # Rotating Top left frame
        img[height // 2:,:width //2] = smaller_frame # Bottom left frame
        img[:height // 2,width //2:] = cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180) # Rotating Top right frame
        img[height // 2:,width //2:] = smaller_frame # Bottom right frame
        cv2.imshow("Webcam",img)
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