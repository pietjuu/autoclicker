#!/usr/bin/python
# -*- coding: utf-8 -*-
import pyautogui
import time
import webbrowser

webbrowser.open("https://www.humanbenchmark.com/tests/number-memory", new=2)
time.sleep(5)

delay = 1
levels = 100

# (width, height) = pyautogui.size()
# print(width, height)
width = 936
height = 694
pyautogui.moveTo(width, height)
color = pyautogui.pixel(width, height)
hexColor = "%02x%02x%02x" % color
# pyautogui.moveTo(width, height)
print(color)
print(hexColor)

if hexColor == "333333":
    print("test1")
    # (x, y) = pyautogui.locateCenterOnScreen("startnum.png")
    pyautogui.click()
    print("test2")
    # pyautogui.click(width, height + 100)
    for w in range(levels):

        print("test3")
        # very simple just copies and pastes the number to the next page

        pyautogui.click(x=width, y=height, clicks=3, interval=.25)


        pyautogui.hotkey("ctrl", "c")
        hexColor = ""
        print("test4")
        while hexColor != "2b2b2b":
            color = pyautogui.pixel(width, height)
            hexColor = "%02x%02x%02x" % color
            print("test5")
            print(hexColor)
        hexColor = ""
        print("testhexcolor")
        pyautogui.hotkey("ctrl", "v")
        print("hotkey")
        pyautogui.press("enter")
        print("enter")
        time.sleep(delay)
        print("test6")
        if w != levels - 1:
            pyautogui.click(937, 625)
            print("test7")
else:
    pyautogui.alert(
        text="error"
        , title="Game not detected!", button="Ok")
