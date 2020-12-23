#John Hua - Cursor Position
#
#Returns the x and y coordinates of cursor position on the screen.
#For debugging purposes only.
#
#9.05.2020

from pyautogui import * 
import pyautogui 
from selenium import webdriver
import time 
import keyboard 
import random
import win32api, win32con

while 1:
    
    coords = pyautogui.position()
    print(coords)
    sleep(1)
