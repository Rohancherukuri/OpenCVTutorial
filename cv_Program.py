import cv2
from random import randint

def main():
    """This is main function"""
    IMG_PATH = "Assets/LordHanuman.jpg"
    SECOND_IMG_PATH = "Assets/Demon-Slayer-Tanjiro-Spider-Man-meme.jpg"
    img = cv2.imread(IMG_PATH)
    resized_img = cv2.resize(img,(0,0),fx = 0.75,fy = 0.75)
    # new_img = cv2.imread(SECOND_IMG_PATH)
    # rotated_img = cv2.rotate(new_img,cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow("Lord Hanuman image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def anotherFunc():
    img_path = "Assets/traveler.png"
    img = cv2.imread(img_path)
    print(f"The height is {img.shape[0]}, width is {img.shape[1]} and number of channels are {img.shape[2]} of the image!")
    # A channel is a color space of the image used in the program
    # OpenCV uses BGR color format instead of RGB standard color set
    # print(img[27][90])
    for i in range(100):
        for j in range(img.shape[1]):
            img[i][j] = [randint(0,255),randint(0,255),randint(0,255)]
    
    cv2.imshow("Transformed Image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    try:
        main()
        #anotherFunc()
    
    except Exception as e:
        print("Sorry there was an error in your code: "+str(e))