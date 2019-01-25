import time
#used for sleeping the process
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url ='https://twitter.com/login'
#stores the url first
browser=webdriver.Chrome()
#get Chrome out
browser.maximize_window()
#maximize chrome window
browser.get(url)
#goto login page
time.sleep(1)
#sleep for elements to load
username=browser.find_element_by_class_name("js-username-field")
# the original field is js-username-field email-input js-initial-focus
# the arguments f**ked the methods and it cant return the correct field
password=browser.find_element_by_class_name("js-password-field")
#get the element of password field
username.clear()
username.send_keys('username here', Keys.TAB)
password.clear()
password.send_keys('password here', Keys.ENTER)
