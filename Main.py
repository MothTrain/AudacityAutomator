import configparser
import sys
import time

import keyboard
import mouse


if sys.argv.__len__() < 2:
    configPath = input("script file path not specified: Enter path: ")
else:
    configPath = sys.argv[1]

configFile = open(configPath, 'r')


while True:
    line = configFile.readline()
    if line == '': break # End of file

    line = line.removesuffix('\n')
    if line == '': continue # Empty line

    split = line.split(' ', 1)

    operator = split[0]
    argument = split[1]
    if split.__len__() != 2:
        print(f"Not 2 arguments: {line}")
        continue

    if operator == "TYPE":
        keyboard.write(argument)

    elif operator == "PRESSEDTYPE":
        chars = list(argument)
        for char in chars: keyboard.press_and_release(char)

    elif operator == "PRESS":
        keyboard.press_and_release(argument)

    elif operator == "PRESSSCAN":
        scanCode = int(argument)
        keyboard.press_and_release(scanCode)

    elif operator == "WAIT":
        millis = int(argument)/1000
        time.sleep(millis)

    elif operator == "WAITFOR":
        keyboard.wait(argument)

    elif operator == "CLICK":
        x, y = argument.split(" ")
        mouse.move(x, y)
        mouse.click('left')

    elif operator == "//":
        continue
    else:
        print(f"Invalid operator: {split[0]}")


configFile.close()

