import requests
import json
import string
import random
import time

#names = json.loads(open('names.json','r').read())
contents=json.loads(open('content.json',encoding='utf-8').read())
url='https://docs.google.com/forms/d/e/1FAIpQLSfPcxRjEbGq5qo5lcHUWZjLcOSeBfScNUH48jMSubgPst-5zQ/formResponse'
for x in range(1000):
    #name_extra=''.join(random.choice(string.digits) for x in range(3))
    #email=name+name_extra+"@gmail.com"
    content = random.choice(contents)
    requests.post(url, allow_redirects=False, data={
    #'emailAddress': email,
    'entry.673033949': content
    })
    print (f'Sending {content}')
    time.sleep(4)
