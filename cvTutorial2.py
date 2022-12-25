import cv2
from time import time

def main():
    """This is main method"""
    try:
        cam = cv2.VideoCapture(0)
        cam.set(3,640) # setting the width
        cam.set(4,480) # setting height
        while cam.isOpened():
            rect,frame = cam.read()
            cv2.imshow("WebCam",frame)
            if cv2.waitKey(10) == ord("q"):
                break
    except Exception as e:
        print("Error occured: "+str(e))

if __name__ == "__main__":
    try:
        t1 = time()
        main()
        t2 = time()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t3 = t2 - t1
        print("[Finished in: "+str(round(t3,3))+" sec]")