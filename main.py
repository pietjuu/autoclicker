#!/usr/bin/python

# Import modules
import pyautogui
import time
import webbrowser

# Open the web browser
webbrowser.open('https://www.humanbenchmark.com/tests/reactiontime', new=2)
time.sleep(10)  # time to open the browser

# variables
delay = 0
levels = 5

# calculate screensize and position to click
(width, height) = pyautogui.size()
print(width, height)
width = int(width / 2)
height = int(height / 4)
pyautogui.moveTo(width, height)

