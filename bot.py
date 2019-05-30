from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *


class Cordinates():
    replaybtn = (960, 650)
    dinosaur = (526, 671)
    clock_strt = 0


def restartGame():
    pyautogui.click(Cordinates.replaybtn)
    Cordinates.clock_strt = time.time()


def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.04)
    pyautogui.keyUp('space')


def addSpeed():
    t = time.time()-Cordinates.clock_strt
    return t*t/47


def imageGrab():
    box = (Cordinates.dinosaur[0]+20, Cordinates.dinosaur[1]-20, Cordinates.dinosaur[0]+328+addSpeed(), Cordinates.dinosaur[1]+30)
    image = ImageGrab.grab(box)
    gray_image = ImageOps.grayscale(image)
    a = array(gray_image.getcolors())
    print(a.sum())
    #print("czas "+str(time.time()))
    # print("przyspieszenie "+str(330+addSpeed()))
    return a.sum()


def main():
    restartGame()
    while True:
        if(imageGrab() >= 22000+(time.time()-Cordinates.clock_strt)*50):
            print(22000+(time.time()-Cordinates.clock_strt)* 50)
            pressSpace()
            time.sleep(0.01)


main()