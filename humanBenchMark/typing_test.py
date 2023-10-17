#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Import modules
import pyautogui
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from pynput.mouse import Button, Controller

# Set up the driver
driver = webdriver.Chrome()
url = "https://humanbenchmark.com/tests/typing"
driver.get(url)

# Wait for the page to load
time.sleep(5)

# get the page source
html = driver.page_source

# create a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")
spans = soup.find_all("span", class_="incomplete")
text_to_type = "".join([span.get_text() for span in spans])

# Wait some time to prevent that weird stuff happens
time.sleep(1)

# click the text box
mouse = Controller()
mouse.position = (879, 527)
mouse.click(Button.left, 1)

# type the text
pyautogui.typewrite(text_to_type, interval=0)

# Wait for the user to press enter to close the browser
input("Press Enter to continue...")
