import cv2
import numpy as np
import time
import os

def main():
    """This is a main function"""
    IMG_PATH  = "/home/rohanoxob/Desktop/LordHanuman.jpg"
    img = cv2.imread(IMG_PATH)
    print("The image in matrix form is:\n",img)
    time.sleep(1)
    os.system("clear")

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