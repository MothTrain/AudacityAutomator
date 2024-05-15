"""DEPRECATED
This is a demonstration of an automation without script files"""


import configparser
import sys
import time

import keyboard

if (sys.argv[1] is None):
    print("No run configuration was specified!")

configFile = open(sys.argv[1])

keyboard.wait('ctrl+alt+b')

time.sleep(1)

keyboard.press_and_release('ctrl+o')

time.sleep(1.5)
keyboard.write(sys.argv[1])
keyboard.press_and_release('enter')

time.sleep(3)
keyboard.press_and_release('ctrl+shift+e')
time.sleep(1.5)
keyboard.write(sys.argv[2], 0.01)
keyboard.press_and_release('enter')
time.sleep(0.5)
keyboard.press_and_release('enter')
time.sleep(0.5)
keyboard.press_and_release('enter')




