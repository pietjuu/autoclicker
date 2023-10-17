#!/usr/bin/python
# -*- coding: utf-8 -*-


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

while write_count < max_Write:
    # state 1
    number = ""
    while number in ["", " "]:
        number = get_number()

    # state 2
    while get_number() not in ["", " "]:
        pass

    # state 3
    pyautogui.typewrite(number, interval=0)

    # click submit
    mouse.position = (943, 674)
    mouse.click(Button.left, 1)

    # click next
    mouse.position = (945, 756)
    mouse.click(Button.left, 1)
    write_count += 1
    # clear the number
    number = ""

input("Press Enter to continue...")
