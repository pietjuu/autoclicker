import cv2
import numpy as np
import pyautogui
import webbrowser
import time
from pynput.mouse import Button, Controller

# Open the web browser
webbrowser.open("https://humanbenchmark.com/tests/sequence", new=2)
time.sleep(5)  # time to open the browser

mouse = Controller()

time.sleep(1)
mouse.position = (944, 673)
mouse.click(Button.left, 1)

time.sleep(1)
# Coordinates of the rectangle
# top_left = (563, 260) number memory
# bottom_right = (1340, 360) number memory

# sequence memory
top_left = (711, 312)
bottom_right = (1184, 784)

# Color of the rectangle (red in BGR format)
color = (0, 0, 255)  # (B, G, R)

# Capture a screenshot of the current screen
screenshot = pyautogui.screenshot()

# Convert the screenshot to an OpenCV image
screenshot = np.array(screenshot)
screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

# Draw the red rectangle on the screenshot
cv2.rectangle(screenshot, top_left, bottom_right, color, thickness=2)

# Display the screenshot with the red rectangle
cv2.imshow("Screenshot with Rectangle", screenshot)

# Save the screenshot with the rectangle
cv2.imwrite("screenshots_with_rectangles/screenshot_with_rectangle_sequence_memory.png", screenshot)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
