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


"""
def check_if_number_is_on_the_screen():
    soup = get_soup(driver)
    divs = soup.find_all("div", class_="big-number")
    if not divs:
        print("number is gone")
        return True  # list is empty so number is gone
    else:
        print("number is still there")
        return False

"""


def get_number():
    soup = get_soup(driver)
    divs = soup.find_all("div", class_="big-number")
    number = "".join([div.get_text() for div in divs])
    return number


# Wait some time to prevent that weird stuff happens
time.sleep(1)

# click the text box
mouse = Controller()
mouse.position = (947, 735)
mouse.click(Button.left, 1)
time.sleep(0.5)

write_count = 0
max_Write = 250

# TODO check if number is still there, when it is gone write the number down (check html)
while write_count < max_Write:
    # Re-fetch the spans inside the loop to reflect the updated content
    """
    soup = get_soup(driver)
    divs = soup.find_all("div", class_="big-number")
    number = "".join([div.get_text() for div in divs])
    """
    # state 1
    number = ""
    while number in ["", " "]:
        number = get_number()

    # state 2
    while get_number() not in ["", " "]:
        pass

    # state 3
    #time.sleep(0.1)
    pyautogui.typewrite(number, interval=0)

    #time.sleep(0.1)
    mouse.position = (943, 674)
    mouse.click(Button.left, 1)
    #time.sleep(0.1)

    mouse.position = (945, 756)
    mouse.click(Button.left, 1)
    #time.sleep(0.1)
    write_count += 1
    number = ""

input("Press Enter to continue...")
