#John Hua - Auto Battler Beta
#
#Automates battling against bots using image
#recognition to detect where to press next in the battle sequence.
#
#Instructions: Press 'Q' to start/end the bot
#10.24.2020

from pyautogui import * 
import pyautogui
import pydirectinput
import time 
import keyboard 
import random
import win32api, win32con

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

battle = False
arrow = False
battleCount = 0

while keyboard.is_pressed('del') == False:

    if keyboard.is_pressed('q') == True:
        while keyboard.is_pressed('q') == True:
            time.sleep(0.02)
        battle = not battle
        print(battle)

    s = random.uniform(0.0, 0.2)
    x = random.uniform(-3.0, 6.0)
    y = random.uniform(-1.0, 4.0)

    if (battle == True):
        time.sleep(0.5)
        if pyautogui.locateCenterOnScreen('Attack_close.png', confidence=0.8) != None:
            cent = pyautogui.locateCenterOnScreen('Attack_close.png', confidence=0.8)
            pyautogui.moveTo(cent[0]+x, cent[1]+y)
            pydirectinput.click()
        elif pyautogui.locateCenterOnScreen('Continue_close.png', confidence=0.8) != None:
            cent2 = pyautogui.locateCenterOnScreen('Continue_close.png', confidence=0.8)
            pyautogui.moveTo(cent2[0]+x, cent2[1]+y)
            pydirectinput.click()
        elif pyautogui.locateCenterOnScreen('Rebattle.png', confidence=0.9) != None:
            cent4 = pyautogui.locateCenterOnScreen('Rebattle.png', confidence=0.9)
            pyautogui.moveTo(cent4[0]+x, cent4[1]+y)
            pydirectinput.click()
            battleCount += 1
            print(battleCount)
    else:
        time.sleep(0.1)


    
