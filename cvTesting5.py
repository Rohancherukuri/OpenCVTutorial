import numpy as np
import cv2


def myFunc():
    VIDEO_PATH = "Assets/ScorpionKick.mp4"
    cam = cv2.VideoCapture(VIDEO_PATH)
    cam.set(3, 160)
    cam.set(4,120)
    
    if not cam.isOpened():
        raise Exception("Could not open the video!")
    
    while cam.isOpened():
        x,video = cam.read()
        cv2.imshow("Scoripion Kick",video)
        
        if cv2.waitKey(8) == ord("q"):
            break
    cam.release()
    cv2.destroyAllWindows()

def main():
    try:
        myFunc()
    
    except Exception as e:
        print("Error occurred: "+str(e))


if __name__ == "__main__":
    try:
        main()
    
    except Exception as e:
        print("sorry there was an error in your code: "+str(e))