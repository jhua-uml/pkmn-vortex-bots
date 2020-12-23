#John Hua - Auto-Catcher
#
#Uses Selenium to scrape the browser game's webpage to look
#for a certain Pokemon's name by using the find_element function
#locate the text by xpath. Sends the user a text message when the
#element or in this case the Pokemon's name appears on the webpage.
#
#10.03.2020


from pyautogui import * 
import pyautogui
import pydirectinput
import time 
import keyboard 
import random
import win32api, win32con

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from twilio.rest import Client
account_sid = 'AC80ef57ec0539c1e39d4b5edc60457387'
auth_token = '86a907a22209b6d3fbbf9459e2ed1f37'
client = Client(account_sid, auth_token)

driver = webdriver.Firefox()
driver.get('https://www.pokemon-vortex.com/')

from twilio.rest import Client
account_sid = 'AC80ef57ec0539c1e39d4b5edc60457387'
auth_token = '86a907a22209b6d3fbbf9459e2ed1f37'
client = Client(account_sid, auth_token)

pkmn = False
arrow = False
txtCount = 0

while keyboard.is_pressed('del') == False:

    if keyboard.is_pressed('q') == True:
        while keyboard.is_pressed('q') == True:
            time.sleep(0.02)
        pkmn = not pkmn
        print(pkmn)

    if pkmn == True:
        #if driver.find_element_by_xpath("//div[@id='pkmnappear']//*[contains(text(), 'Searching')]"):
        try:
            driver.find_element_by_xpath("//div[@id='pkmnappear']//*[contains(text(), 'Shiny Celesteela') or \
                                            contains(text(), 'Metallic Celesteela') or \
                                            contains(text(), 'Shadow Celesteela') or \
                                            \
                                            contains(text(), 'Shiny Darkrai') or \
                                            contains(text(), 'Shadow Darkrai') or \
                                            contains(text(), 'Metallic Darkrai') or \
                                            contains(text(), 'Dark Darkrai') or \
                                            contains(text(), 'Mystic Darkrai') or \
                                            \
                                            contains(text(), 'Shiny Darkrown') or \
                                            contains(text(), 'Shadow Darkrown') or \
                                            contains(text(), 'Metallic Darkrown') or \
                                            contains(text(), 'Dark Darkrown') or \
                                            contains(text(), 'Mystic Darkrown') or \
                                            \
                                            contains(text(), 'Shiny Genesect') or \
                                            contains(text(), 'Shadow Genesect') or \
                                            contains(text(), 'Metallic Genesect') or \
                                            contains(text(), 'Dark Genesect') or \
                                            contains(text(), 'Mystic Genesect') or \
                                            \
                                            contains(text(), 'Shiny Jirachi') or \
                                            contains(text(), 'Shadow Jirachi') or \
                                            contains(text(), 'Metallic Jirachi') or \
                                            contains(text(), 'Dark Jirachi') or \
                                            contains(text(), 'Mystic Jirachi') or \
                                            \
                                            contains(text(), 'Shiny Meltan') or \
                                            contains(text(), 'Shadow Meltan') or \
                                            contains(text(), 'Metallic Meltan') or \
                                            contains(text(), 'Dark Meltan') or \
                                            contains(text(), 'Mystic Meltan') or \
                                            \
                                            contains(text(), 'Shiny Raikou') or \
                                            contains(text(), 'Shadow Raikou') or \
                                            contains(text(), 'Metallic Raikou') or \
                                            contains(text(), 'Dark Raikou') or \
                                            contains(text(), 'Mystic Raikou') or \
                                            \
                                            contains(text(), 'Shiny Darkrai') or \
                                            contains(text(), 'Shadow Darkrai') or \
                                            contains(text(), 'Metallic Darkrai') or \
                                            contains(text(), 'Dark Darkrai') or \
                                            contains(text(), 'Mystic Darkrai') or \
                                            \
                                            contains(text(), 'Tapu') or \
                                            contains(text(), 'Shiny Thundurus') or \
                                            contains(text(), 'Shadow Thundurus') or \
                                            contains(text(), 'Metallic Thundurus') or \
                                            contains(text(), 'Dark Thundurus') or \
                                            contains(text(), 'Mystic Thundurus') or \
                                            \
                                            contains(text(), 'Shiny Xurkitree') or \
                                            contains(text(), 'Shadow Xurkitree') or \
                                            contains(text(), 'Metallic Xurkitree') or \
                                            contains(text(), 'Dark Xurkitree') or \
                                            contains(text(), 'Mystic Xurkitree') or \
                                            \
                                            contains(text(), 'Shiny Zapdos') or \
                                            contains(text(), 'Shadow Zapdos') or \
                                            contains(text(), 'Metallic Zapdos') or \
                                            contains(text(), 'Dark Zapdos') or \
                                            contains(text(), 'Mystic Zapdos') or \
                                            \
                                            contains(text(), 'Shiny Zekrom') or \
                                            contains(text(), 'Shadow Zekrom') or \
                                            contains(text(), 'Metallic Zekrom') or \
                                            contains(text(), 'Dark Zekrom') or \
                                            \
                                            contains(text(), 'Mystic Zekrom')]")
            print("Pokemon found.")
            name = driver.find_element_by_xpath("//div[@id='pkmnappear']//*[contains(text(), 'Wild')]")
            print (name.text)
            if txtCount == 0:
                name = driver.find_element_by_xpath("//div[@id='pkmnappear']//*[contains(text(), 'Wild')]")
                message = client.messages \
                .create(
                        body=name.text,
                        from_='+0', #Phone number redacted
                        to='+0' #Phone number redacted
                   )
                print(name)
                txtCount += 1
            time.sleep(0.5)
        except NoSuchElementException:
            try:
                driver.find_element_by_xpath("//div[@id='pkmnappear']//*[contains(text(), 'Searching')]")
                print("Waiting...")
                time.sleep(1.5)
            except NoSuchElementException:
                print("Not found.")
                txtCount = 0
                if arrow == True:
                    pydirectinput.keyDown('left')
                    arrow = not arrow
                    time.sleep(0.3)
                else:
                    pydirectinput.keyDown('right')
                    arrow = not arrow
                    time.sleep(0.3)
    else:
        time.sleep(0.025)


    
