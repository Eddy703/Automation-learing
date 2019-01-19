from selenium import webdriver
import time
import os
#grabbing the information user wants to google
search=input("What do you want to search?\n")

#open browser and google automatically
if search is not '':
    browser = webdriver.Chrome()
    browser.get('https://google.com')
    time.sleep(1)
    assert "Google" in browser.title
    elem=browser.find_element_by_name("q");
    elem.clear()
    elem.send_keys(search)
    #elem.send_keys(Keys.RETURN)
    elem.submit()
    os.system('cls')
    print(f'Done')
