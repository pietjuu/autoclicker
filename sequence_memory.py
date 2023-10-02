#!/usr/bin/python
# -*- coding: utf-8 -*-

# Import modules
import pyautogui
import time


def compute_positions(top_left, bottom_right):
    width = (bottom_right[0] - top_left[0]) // 2
    height = (bottom_right[1] - top_left[1]) // 2

    positions_ = [
        (top_left[0], top_left[1]),
        (top_left[0] + width, top_left[1]),
        (bottom_right[0], top_left[1]),
        (top_left[0], top_left[1] + height),
        (top_left[0] + width, top_left[1] + height),
        (bottom_right[0], top_left[1] + height),
        (top_left[0], bottom_right[1]),
        (top_left[0] + width, bottom_right[1]),
        (bottom_right[0], bottom_right[1])
    ]

    return positions_


# coordinates 3 x 3 grid
# TODO find right coordinates
top_left_ = (711, 312)
bottom_right_ = (1185, 784)

positions = compute_positions(top_left_, bottom_right_)
print(positions)
flash_list = []
last_flash_time = None
print("script started")
try:
    while True:
        print("checking")
        for idx, pos in enumerate(positions):
            # color is white
            print("check2")
            if pyautogui.pixelMatchesColor(pos[0], pos[1], (255, 255, 255)):
                print("white")
                # check for duplicates
                if len(flash_list) == 0 or flash_list[-1] != idx:
                    flash_list.append(idx)
                    last_flash_time = time.time()
                    print(flash_list)
        # if 3 seconds have passed since the last flash, click the positions
        if last_flash_time and (time.time() - last_flash_time) > 3:
            for idx in flash_list:
                pyautogui.click(positions[idx][0], positions[idx][1])
                print("Clicked position", idx)
                print(flash_list)
            flash_list.clear()
            print("Cleared list")
            last_flash_time = None

        time.sleep(0.1)  # this checks 10 times a second

except KeyboardInterrupt:
    print("script stopped")
