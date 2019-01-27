import time
#used for sleeping the process
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import json
proof=random.random()
url ='https://twitter.com/login'
#stores the url first
with open('user.txt',encoding='utf-8') as file:
    user=json.load(file)
for key, val in user.items():
    user=key
    pw=val
    browser=webdriver.Chrome()
    #get Chrome out
    browser.maximize_window()
    #maximize chrome window
    browser.get(url)
    #goto login page
    time.sleep(1)
    #sleep for elements to load
    username=browser.find_element(By.CLASS_NAME,"js-username-field")
    # the original field is js-username-field email-input js-initial-focus
    # the arguments f**ked the methods and it cant return the correct field
    password=browser.find_element(By.CLASS_NAME,"js-password-field")
    #get the element of password field
    username.clear()
    username.send_keys(user, Keys.TAB)
    password.clear()
    password.send_keys(pw, Keys.ENTER)
    
    tweet=browser.find_element(By.ID,'tweet-box-home-timeline')
    tweet.clear()
    #Auto write tweet
    tweet.send_keys('This is a tweet automated by Python using selenium.\n')
    tweet.send_keys(f'For every automated tweet a random number will be posted:\n{proof} \n')
    tweet.send_keys('Learn more on: \nhttps://github.com/Eddy703/Automation-learning\n')
    #click on tweet button and tweet!
    browser.find_element(By.CSS_SELECTOR,'button.tweet-action').click()
    browser.close()
