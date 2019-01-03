from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import csv
from lxml.html import parse

params = {'func': 'login-session',
            'login_source': 'bor-info',
            'bor_id': 1670766,
            'bor_verification': 670766,
            'bor_library': 'NEU50'}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Language": "zh-CN,zh;q=0.8"}

html = urlopen("http://202.118.8.7:8991/F/-?func=bor-info")
loginPage = BeautifulSoup(html.read(), "html.parser")
loginUrl = loginPage.find("form", {'name': 'form1'})
print(loginUrl['action'])
r = requests.post(loginUrl['action'], data=params, headers=headers)
# print(r.content.decode('utf-8'))

csvFile = open("../lib_info/personalInfo.csv", 'w+', newline='', encoding='utf-8')
# myInfo = BeautifulSoup(r.content.decode('utf-8'), "html.parser")
myInfo = parse(r.content.decode('utf-8'))
doc = myInfo.getroot()

links = doc.findAll('.//table')
# baseInfo = myInfo.find("table")
# baseInfo = myInfo.find("table", {"class", "indent1"}).findAll("td")
# print(baseInfo)

# print(myInfo.text)

