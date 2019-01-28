import requests
import json
import string
import random
import time

names  =  json.loads(open('names.json','r').read())
contents = json.loads(open('content.json',encoding = 'utf-8').read())
users = json.loads(open('user.txt',encoding = 'utf-8').read())
url = 'https://docs.google.com/forms/d/e/1FAIpQLSc_77-z54kT28t8zbweKQU4AKyXetmSBxL2EmQrzT4IHSUE-w/formResponse'
s =  requests.session()
#print (random.choice(list(users.keys())))
while (1):
    NoNeedEmail =True
    user = random.choice(list(users.keys()))
    pw = users[user]
    s.auth = (user,pw)
    name  =  random.choice(names)
    name_extra  =  ''.join(random.choice(string.digits) for x in range(3))
    email  =  name + name_extra + "@mailinator.com"
    content  =  random.choice(contents)
    if (NoNeedEmail):
        k=s.post(url, allow_redirects  =  False, data = {
        'entry.1042087874': content
        })
    if not(NoNeedEmail):
        s.post(url, allow_redirects  =  False, data = {
        'emailAddress': email,
        'entry.1042087874': content
        })
    if not(k.status_code == 200):
        NoNeedEmail=False
    print (f'Sending from {user} with {content}')
    print (k.status_code)
    time.sleep(3)
