import requests
import json
import string
import random

names = json.loads(open('names.json','r').read())
url='https://docs.google.com/forms/d/e/1FAIpQLSfPcxRjEbGq5qo5lcHUWZjLcOSeBfScNUH48jMSubgPst-5zQ/formResponse'
for name in names:
    name_extra=''.join(random.choice(string.digits) for x in range(3))
    email=name+name_extra+"@gmail.com"
    content = "...校方很聰明 粵華政治學社提交匿名要google登入 大家注意 這是學校的騙局 一登入google再提交匿名到粵華政治學社 身份會被公開 粵華政治學社就是校方設立的釣魚台"
    requests.post(url, allow_redirects=False, data={
    'emailAddress': email,
    'entry.673033949': content
    })
    print (f'Sending {email} and {content}')
