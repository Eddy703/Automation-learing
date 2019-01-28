#This py file only works on single text field
#And this particular file targets a specific form made by so called @yw_politics_association on instagram
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url= 'https://docs.google.com/forms/d/e/1FAIpQLSc_77-z54kT28t8zbweKQU4AKyXetmSBxL2EmQrzT4IHSUE-w/viewform'
#Prompt the user the enter the number of time to spam the form
num_times=input("Enter the number of time you want to spam: ")
#Prompt the user to enter the content to spam
text=input("Enter the text you want to spam: ")

for i in range(1,int(num_times)+1):
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    driver.get(url)
    #Goto the Link
    text_field=driver.find_element_by_xpath('//textarea[@class="quantumWizTextinputPapertextareaInput exportTextarea"]')
    text_field.send_keys(text)
    #Find the button
    submitbtn=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div/content')
    submitbtn.click()
    #close the browser
    driver.close()
    print(f'Done! {i} '+("times. " if i>1 else "time. "))
