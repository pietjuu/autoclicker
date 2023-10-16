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
url = "https://humanbenchmark.com/tests/verbal-memory"
driver.get(url)

# Wait for the page to load
time.sleep(5)

# get the page source
html = driver.page_source

# create a BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")
spans = soup.find_all("div", class_="word")

# Wait some time to prevent that weird stuff happens
time.sleep(1)

# add word to set, if word is already in set, click "SEEN", else click "NEW"
seen_words = set()
for span in spans:
    word = span.get_text()
    if word in seen_words:
        pyautogui.click(1071, 524)
    else:
        pyautogui.click(1071, 524)
        seen_words.add(word)
    time.sleep(0.1)