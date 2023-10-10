#!/usr/bin/python
# -*- coding: utf-8 -*-
# import modules
import pyautogui
import threading
import keyboard

# Define the target color in RGB format
target_color = (255, 255, 255)

pyautogui.FAILSAFE = False

# Flag to signal the thread to stop
stop_thread = False


# Function to check for the failsafe key press
def check_failsafe():
    global stop_thread
    if keyboard.is_pressed('esc'):
        print("Program terminated by user.")
        stop_thread = True


# Function to continuously check the screen for the target color
def check_screen():
    global stop_thread
    while True:
        if stop_thread:
            break  # TODO Exit the loop if the failsafe is activated
        screenshot = pyautogui.screenshot()

        for x in range(screenshot.width):
            for y in range(screenshot.height):
                pixel_color = screenshot.getpixel((x, y))

                # Check if the pixel color matches the target color (black)
                if pixel_color == target_color:
                    # Click the pixel if the color matches
                    pyautogui.click(x=x, y=y)
                    print("Pixel clicked at coordinates:", x, y)


# Start the screen-checking thread
screen_check_thread = threading.Thread(target=check_screen)
screen_check_thread.start()

# Check for the failsafe key press in the main thread
while True:
    check_failsafe()
    if stop_thread:
        break  # Exit the loop when the failsafe is activated

# Set the flag to stop the screen-checking thread
stop_thread = True

# Wait for the screen-checking thread to finish
screen_check_thread.join()
