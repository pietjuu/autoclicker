#!/usr/bin/python
# -*- coding: utf-8 -*-
# TODO check if coordinates are correct and if pixels are correct

# Import modules
import pyautogui
import time
import webbrowser
import shlex
import sys
import time
import cv2
import numpy as np
import mss
from itertools import islice
from pynput.mouse import Button, Controller
import pytesseract
import threading
import keyboard

"""
# Open the web browser
webbrowser.open("https://www.humanbenchmark.com/tests/number-memory", new=2)
time.sleep(5)

"""

# create an empty set to store the coordinates of the white boxes
white_box_coordinates = set()
# set path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# store empty string in flag
flag = ""
# store True in flag2
flag2 = True
# create a set from and store in flag3
flag3 = set()
# instantiate of controller class for monitoring mouse and keyboard
mouse = Controller()

time.sleep(1)
mouse.position = (950, 444)
mouse.click(Button.left, 1)


def get_number():
    global flag, flag2, flag3, flag4
    while True:
        stc = mss.mss()  # create an instance of mss class
        scr = stc.grab(  # grab the screen
            {
                "left": 563,
                "top": 260,
                "width": 777,
                "height": 100,
            }
        )
        frame = np.array(scr)
        # using morphology to remove noise from the image and convert it to black and white
        hsvframe = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        thresh = cv2.threshold(hsvframe, 220, 255, cv2.THRESH_BINARY)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        result = 255 - close
        # optical character recognition on result for getting the number
        a = pytesseract.image_to_boxes(result, config="--oem 3 --psm 6 outputbase digits")
        flag = "".join([x.split()[0] for x in a.splitlines() if x.split()[0].isdigit()])
        print(flag)
        if flag2 == False or keyboard.is_pressed("q"):
            break


# using threading because so that it doesn't block opencv loop
threading.Thread(target=get_number).start()


def clicker():
    points = list(white_box_coordinates)
    for i in points:
        mouse = Controller()
        mouse.position = (i[0] + 744, i[1] + 130)
        mouse.click(Button.left, 1)



