#!/usr/bin/python
# Import modules
import pyautogui
import time
import webbrowser

# Open the web browser
webbrowser.open("https://www.humanbenchmark.com/tests/reactiontime", new=2)
time.sleep(5)  # time to open the browser

# variables
delay = 0
levels = 5

# calculate screensize and position to click
(width, height) = pyautogui.size()
width = int(width / 2)
height = int(height / 4)

pyautogui.moveTo(width, height)


def autoclick():
    # gets the current hex color of the game
    color = pyautogui.pixel(width, height)
    hexColor = "%02x%02x%02x" % color

    if hexColor == "2b87d1":
        pyautogui.click()
        for x in range(levels):
            # checks every time if the color is not green,
            # when it is green it delays and then clicks the screen and waits for the next round
            while hexColor != "4bdb6a":
                color = pyautogui.pixel(width, height)
                hexColor = "%02x%02x%02x" % color
            time.sleep(delay)
            pyautogui.click()
            if x != 4:
                pyautogui.click()
            hexColor = ""

    else:
        pyautogui.alert(
            text="error", title="Game not detected!", button="Ok")


autoclick()
