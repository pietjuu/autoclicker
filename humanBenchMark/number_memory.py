#!/usr/bin/python
# -*- coding: utf-8 -*-
# TODO check if coordinates are correct and if pixels are correct

"""
read html for number and add it in list and write it down
"""

# Import modules
import pyautogui
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from pynput.mouse import Button, Controller

# Set up the driver
driver = webdriver.Chrome()
url = "https://humanbenchmark.com/tests/number-memory"
driver.get(url)

# Wait for the page to load
time.sleep(5)
pyautogui.FAILSAFE = False


# create a BeautifulSoup object
def get_soup(driver):
    return BeautifulSoup(driver.page_source, "html.parser")


# Wait some time to prevent that weird stuff happens
time.sleep(1)

# click the text box
mouse = Controller()
mouse.position = (947, 735)
mouse.click(Button.left, 1)
time.sleep(0.5)

write_count = 0
max_Write = 250

while write_count < max_Write:
    # Re-fetch the spans inside the loop to reflect the updated content
    soup = get_soup(driver)
    divs = soup.find_all("div", class_="big-number")
    print(divs)
    number = "".join([div.get_text() for div in divs])
    print(number)
    print("test")
    time.sleep(4)
    if number:
        print(number)

        pyautogui.typewrite(number, interval=0)

        mouse.position = (943, 674)
        mouse.click(Button.left, 1)
        time.sleep(2)

        mouse.position = (945, 756)
        mouse.click(Button.left, 1)
        time.sleep(2)

        write_count += 1
    else:
        break

input("Press Enter to continue...")
