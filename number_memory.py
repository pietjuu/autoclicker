#!/usr/bin/python
# -*- coding: utf-8 -*-
# Import modules
import pyautogui
import time
import webbrowser
import shlex
import sys
import time
import cv2
import numpy as np
import mss
from itertools import islice
from pynput.mouse import Button, Controller
import pytesseract
import threading
import keyboard

# Open the web browser
webbrowser.open("https://www.humanbenchmark.com/tests/number-memory", new=2)
time.sleep(5)
