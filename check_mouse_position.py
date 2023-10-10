#!/usr/bin/python
# -*- coding: utf-8 -*-
# import modules
import pyautogui

try:
    while True:
        # Get the current position of the mouse cursor
        current_position = pyautogui.position()

        # Print the cursor's x and y coordinates
        print("Mouse Cursor Position: x =", current_position[0], ", y =", current_position[1])

except KeyboardInterrupt:
    # Exit the loop when you press Ctrl+C
    pass
