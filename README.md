# autoclicker

## table of contents

1. [setup project](#setup-project)
2. [reaction_time.py](#reaction_timepy)
3. [aim_practice.py](#aim_practicepy)
4. [auto_clicker_fun.py](#auto_clicker_funpy)
5. [check_mouse_position.py](#check_mouse_positionpy)
6. [draw_rectangle.py](#draw_rectanglepy)
7. [number_memory.py](#number_memorypy)
8. [sequence_memory.py](#sequence_memory)
9. [typing_test.py](#typing_testpy)
10. [verbal_memory.py](#verbal_memorypy)

## setup project
To set up the project run the following command in the terminal:\
`git clone https://github.com/pietjuu/autoclicker.git` \
The projects will be stored in different directories named: helpScripts and humanBenchMark.

When the project is cloned, run the following command to install the required packages:\
`pip3 install -r requirements.txt`

## reaction_time.py
This script will give you highscores in the reactiontest game on https://humanbenchmark.com/. \
When you run the script, it will automaticly open the website and start. 
There is a 5-second timer in between opening the window and starting to click\
It will clear all the 5 levels and then give you a highscore. It is recommended
to close as mush programs in order to increase the speed.
Speed can also be gained with a monitor that has a better refresh rate.

![](https://github.com/pietjuu/autoclicker/blob/main/images/reactionTest.gif)

## aim_practice.py
This script will give you highscores in the aimpractice game on https://humanbenchmark.com/. \
When you run the script, you will have to open https://humanbenchmark.com/tests/aim in your browser. 
And click "p" on your keyboard. 
Then it will immediatly start clicking on the targets\
It is recommended to close as mush programs in order to increase the speed.
Speed can also be gained with a monitor that has a better refresh rate.

![](https://github.com/pietjuu/autoclicker/blob/main/images/aimtrainer.gif)

## auto_clicker_fun.py
This script is a bit dangerous because it will click every white pixel on the screen.\
`THERE IS NO STOPPING THE SCRIPT EBCAUSE THE FAILSAFE DOESN'T WORK!`\
Therefore there is no gif of this script.

## check_mouse_position.py
This script will print the mouse position in the terminal.\
It will print the position every 0.1 seconds.\
It is useful to find the position of a button or something else on the screen.

![](https://github.com/pietjuu/autoclicker/blob/main/images/checkMousePosition.gif)

## draw_rectangle.py
This script will draw a rectangle on the screen.\
This is useful to find out what part of the screen is actually checked.\
The coordinates are hardcoded in the script. You should replace them with 
your coordinates using the check_mouse_position.py script.\
The output is a screenshot and it is stored in the directory "screenshots_with_rectangles" (see Github). 
The path is also hardcoded in the script. You should change it to your own path.

Note: the script was designed to check if I was checking the right area of the screen in the sequence memory 
on humanbenchmark.com. So it will open that website and start that game and take a screenshot.

![](https://github.com/pietjuu/autoclicker/blob/main/images/drawRectangle.gif)

## number_memory.py
This script will recongnize the numbers on the screen and fill them in.\
`THIS SCRIPT IS NOT DONE YET!`\
There is a problem with the image recognition where it sometimes doesn't recognize the number.

## sequince_memory.py
This script will remember the sequence and click the right squares in order.\
`THIS SCRIPT IS NOT DONE YET!`\
There is a problem with the clicking and remembering the sequence.

## typing_test.py
This script will give you highscores in the typingtest game on https://humanbenchmark.com/. \
When you run the script, it will automaticly open the website and start. 
There is a 5-second timer that will open the page. In that time you need to make sure that the window is fullscreen.
When the page is fully loaded you need to click the coockie message away!


```
TL;DR
1. Make sure the window is fullscreen
2. Click the coockie message away
```
It should look like this:\
![image](https://github.com/pietjuu/autoclicker/blob/main/images/typingTestPicture.png)

The demo is below:\
![](https://github.com/pietjuu/autoclicker/blob/main/images/typingTest.gif)

## verbal_memory.py
This script will give you highscores in the verbal memory game on https://humanbenchmark.com/. \
When you run the script, it will automaticly open the website and start. 
There is a 5-second timer that will open the page. In that time you need to make sure that the window is fullscreen.
When the page is fully loaded you need to click the coockie message away!\
To end the script you need to press "enter" in the terminal.

```
TL;DR
1. Make sure the window is fullscreen
2. Click the coockie message away
```
It should look like this:\
![image](https://github.com/pietjuu/autoclicker/blob/main/images/verbalMemoryPicture.png)

The demo is below:\
![](https://github.com/pietjuu/autoclicker/blob/main/images/verbalMemory.gif)
