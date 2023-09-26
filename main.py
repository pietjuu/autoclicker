#!/usr/bin/python

# Import modules
import pyautogui
import time
import webbrowser

# Open the web browser
webbrowser.open('https://www.humanbenchmark.com/tests/reactiontime', new=2)
time.sleep(5)  # time to open the browser

# variables
delay = 0
levels = 5

# calculate screensize and position to click
(width, height) = pyautogui.size()
print(width, height)
width = int(width / 2)
height = int(height / 4)
pyautogui.moveTo(width, height)

# gets the current hex color of the game
color = pyautogui.pixel(width, height)
hexColor = '%02x%02x%02x' % color
print(hexColor)
if hexColor == '2b87d1':
    print("test")
    pyautogui.click()
    for x in range(levels):
        # checks every time if the color is not green,
        # when it is green it delays and then clicks the screen and waits for the next round
        while hexColor != '4bdb6a':
            print("test while loop")
            print(hexColor)
            color = pyautogui.pixel(width, height)
            hexColor = '%02x%02x%02x' % color
            print("test na calculatie")
            print(hexColor)
        # print(hexColor)
        time.sleep(delay)
        pyautogui.click()
        if x != 4:
            pyautogui.click()
        hexColor = ''
else:
    pyautogui.alert(
        text='error'
        , title='Game not detected!', button='Ok')
