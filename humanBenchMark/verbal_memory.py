#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import modules
import time
import pyautogui
from selenium import webdriver
from bs4 import BeautifulSoup
from pynput.mouse import Button, Controller

# Set up the driver
driver = webdriver.Chrome()
url = "https://humanbenchmark.com/tests/verbal-memory"
driver.get(url)

# Wait for the page to load
time.sleep(5)


# create a BeautifulSoup object
def get_soup(driver):
    return BeautifulSoup(driver.page_source, "html.parser")


# Wait some time to prevent that weird stuff happens
time.sleep(1)

# click the text box
mouse = Controller()
mouse.position = (947, 735)
mouse.click(Button.left, 1)
time.sleep(3)

# Get the current position of the mouse cursor
current_position = pyautogui.position()

# add word to set, if word is already in set, click "SEEN", else click "NEW"
seen_words = set()

# Initialize a counter for the number of clicks
click_count = 0
max_clicks = 1500

while click_count < max_clicks:
    # Re-fetch the spans inside the loop to reflect the updated content
    soup = get_soup(driver)
    spans = soup.find_all("div", class_="word")

    if spans:
        word = spans[0].get_text()

        if word in seen_words:
            mouse.position = (868, 625)
            mouse.click(Button.left, 1)
        else:
            mouse.position = (1031, 625)
            mouse.click(Button.left, 1)
            seen_words.add(word)
        click_count += 1

        # Add a short delay between clicks
        time.sleep(0)
    else:
        break

input("Press Enter to continue...")
