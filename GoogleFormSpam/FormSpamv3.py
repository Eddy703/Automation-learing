import requests
import json
import string
import random
import time
user_agent={
    "referer": "https: // docs.google.com/forms/d/1wHwJ2B2FSwrME8ZYIasU4KUPV2SwjNES10RTKvqgDB0/viewform?edit_requested = true & fbzx = 9069824534376584105",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0 Win64x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
names  =  json.loads(open('names.json','r').read())
contents = json.loads(open('content.json',encoding = 'utf-8').read())
users = json.loads(open('user.txt',encoding = 'utf-8').read())
url = 'https://docs.google.com/forms/d/e/1FAIpQLSc_77-z54kT28t8zbweKQU4AKyXetmSBxL2EmQrzT4IHSUE-w/formResponse'
header={'content-type':'application/x-www-form-urlencoded'}
#print (random.choice(list(users.keys())))
while (1):
    NeedEmail =True
    user = random.choice(list(users.keys()))
    #pw = users[user]
    #s.auth = (user,pw)
    name  =  random.choice(names).lower()
    name_extra  =  ''.join(random.choice(string.digits) for x in range(3))
    email  =  name + name_extra + "@mailinator.com"
    content  =  random.choice(contents)
    if (NeedEmail):
        k=requests.session().post(url, allow_redirects = False, data = {
        "emailAddress": email,
        "entry.1042087874": content
        },header=user_agent)
    if not(NeedEmail):
        requests.session().post(url, allow_redirects = False, data = {
        "entry.1042087874": content
        },header=user_agent)
    if not(k.status_code == 200):
        NeedEmail=False
    print (f'Sending from {user} with {content}')
    print ("Sent" if k.status_code==200 else "Failed")
    #time.sleep(3)
