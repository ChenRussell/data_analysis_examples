from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

params = {'func': 'login-session',
            'login_source': 'bor-info',
            'bor_id': '1670777',
            'bor_verification': '670777',
            'bor_library': 'NEU50'}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Language": "zh-CN,zh;q=0.8"}
# r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
# r = requests.post("http://202.118.8.7:8991/F/-?func=bor-info", data=params, headers=headers)
# r = requests.post("http://202.118.8.7:8991/F/N946GVSA6LB1NV65JCHX4NTJXQDN4N2CEE3MVL4E7EMKUHY7JX-25365", data=params, headers=headers)
# r = requests.post("http://202.118.8.7:8991/F/4MU6RX1P1IMM3V88PTBJC6PDB1GPAQ1SAX5YFYKL3X5K2EF3AH-69772?func=bor-info", data=params)
# print(type(r))
# r = requests.get("http://202.118.8.7:8991/F/4MU6RX1P1IMM3V88PTBJC6PDB1GPAQ1SAX5YFYKL3X5K2EF3AH-69772?func=bor-info")
# print(r.content.decode('utf-8'))

# html = urlopen("http://202.118.8.7:8991/F/-?func=bor-info")
# html = urlopen("http://localhost:8080/bms-project/")
html = urlopen("https://twitter.com/")
myInfo = BeautifulSoup(html.read(), "html.parser")
print(myInfo)
# loginUrl = myInfo.find("form", {'name': 'form1'})
# loginUrl = myInfo.find("form", {'id': 'formLogin'})
# print(loginUrl['action'])
# print(myInfo.text)
# r = requests.post(loginUrl['action'], data=params, headers=headers)
# print(r.content.decode('utf-8'))
# myInfo = BeautifulSoup(r.content.decode('utf-8'), "html.parser")
# feedback = myInfo.find("div", {"id", "feedbackbar"})
# print(feedback)
# driver = webdriver.PhantomJS(executable_path='../phantomjs-2.1.1-windows/bin/phantomjs')
# d = driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html",data=params)

# session = requests.Session()
#
# s = session.post(loginUrl['action'], data=params, headers=headers)
# print("Cookie is set to:")
# print(s.cookies.get_dict())
#
# print(s.content.decode('utf-8'))