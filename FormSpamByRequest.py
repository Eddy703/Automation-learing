import requests
import string
import random
import os
#stores the url that is going to be connected and send data to
url="https://docs.google.com/forms/d/e/1FAIpQLSc_77-z54kT28t8zbweKQU4AKyXetmSBxL2EmQrzT4IHSUE-w/formResponse"
text=input("Enter the text you want to spam: ")
num= input("Enter the number of time you want to spam: ")
"""Prompt the user to enter the number of spams and the text"""
#char_lst=string.ascii_letters+string.digits+'!@#$%^&*()_+'
#random.seed(os.urandom(1024))
#actual code that sends the text to the url
for i in range(1,int(num)+1):
    #text= ''.join(random.choice(char_lst) for i in range(16))
    requests.post(url,allow_redirects=False,data={
    'entry.1042087874' : text
    })
    #print a message to mark the program is done
    print(f"Done! {i}"+(" time.\n" if i==1 else " times. \n"))
    #print(f"Sending {text}")
