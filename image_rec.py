#John Hua - Image-Recognition Bot
#
#Utilizes image recognition from OpenCV to detect a specified
#image or in this case a Pokemon's name to a confidence interval
#of 80%. Stops and sends a text message to the user using
#Twilio's API when the image is found.
#
#9.14.2020

from pyautogui import * 
import pyautogui
import pydirectinput
import time 
import keyboard 
import random
import win32api, win32con

from selenium import webdriver

from twilio.rest import Client
account_sid = 'AC80ef57ec0539c1e39d4b5edc60457387'
auth_token = '86a907a22209b6d3fbbf9459e2ed1f37'
client = Client(account_sid, auth_token)

def testFunc():
    print("Class found.")
txtCount = 0
pkmn = False

while keyboard.is_pressed('del') == False:

    if keyboard.is_pressed('q') == True:
        while keyboard.is_pressed('q') == True:
            time.sleep(0.02)
        pkmn = not pkmn
        print(pkmn)

    if pkmn == True:
        if  pyautogui.locateOnScreen('insert_pkmn_img.png', confidence=0.8) != None:
            if txtCount == 0:
                message = client.messages \
                    .create(
                        body="Pokemon found.",
                        from_='+0', #Phone number redacted
                        to='+0' #Phone number redacted
                    )
                txtCount += 1
        #Move the character left and right until the image is found.
        else:       
            txtCount = 0
            pydirectinput.keyDown('left')
            time.sleep(0.3)
            pydirectinput.keyUp('left')
            pydirectinput.keyDown('right')
            time.sleep(0.3)
            pydirectinput.keyUp('right')
    else:
        time.sleep(0.025)
                    

    
