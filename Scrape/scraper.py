from bs4 import BeautifulSoup as BS
import requests
import csv
import re

def isArticle(text):
    if re.match('/[A-Za-z]*/[0-9]+/|/[A-Za-z]' ,text):
        return True
    elif re.match('https://',text):
        return True
    return False

r=requests.get("https://www.hk01.com/")
print(r.status_code)
data=r.text
soup=BS(data,'lxml')
#print (soup.prettify())
#href_lst = soup.find_all('span', class_=re.compile("^(sc-)"))
href_lst = set(soup.find_all('a', href=re.compile('/')))
with open('url.csv','w',encoding='utf-8') as f:
    writer=csv.writer(f)
    inlst=[]
    writer.writerow(["Title","URL"])
    for item in href_lst:
        if not(isArticle(item['href'])):
            url="https://www.hk01.com"+item['href']
            sublst=[item.string, url]
            inlst.append(sublst)
    for item in inlst:
        writer.writerow(item)
            #article=requests.get(url)
            #article_soup=BS(article.text,'lxml')
            #print([x for x in article_soup.stripped_strings])
            #con=input("Y to continue N to quit ")
            #if con.upper() in "[Y|y]es":
            #    continue
            #elif con.upper() in "NO":
            #    break
