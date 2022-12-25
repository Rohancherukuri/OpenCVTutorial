# Implementing opencv in python
import cv2
from time import time


def main():
    """This is a main method"""
    try:
        """IMG_PATH = "/home/rohanoxob/My2DGame/traveler.png"
        img = cv2.imread(IMG_PATH)
        cv2.imshow("Img",img)
        cv2.waitKey(1000)"""
        VIDEO_PATH = "/home/rohanoxob/Videos/PardeepDubki.mp4"
        cam = cv2.VideoCapture(VIDEO_PATH)
        cam.set(3,1040) # setting width
        cam.set(4,880) # setting height
        while cam.isOpened():
            success,video = cam.read()
            cv2.imshow("Video",video)
            if cv2.waitKey(35) == ord("q"):
                break
        cam.release()
        cv2.destroyAllWindows()
    
    except Exception as e:
        print("Error occurred: "+str(e))

if __name__ == "__main__":
    try:
        t1 = time()
        main()
        t2 = time()
    
    except (KeyboardInterrupt,Exception) as e:
        print("Sorry there was an error in your code: "+str(e))
    
    finally:
        t3 = t2 - t1
        print("[Finised in: "+str(round(t3,3))+" sec]")