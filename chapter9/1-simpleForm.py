import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

# params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
params = {'bor_id': '1670766', 'bor_verification': '670766'}
# r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
r = requests.post("http://202.118.8.7:8991/F/JUEXYF3AT3M9RUGV1XNAIAG5T1P3GRJ1LGY2I48XVK9F3CCRT4-57137?func=file&file_name=login-session", data=params)
# print(type(r))
# print(r.text)
# print(r.content.decode('utf-8'))
# print(type(r.text))
libraryInfo = bs(r.content.decode('utf-8'), "html.parser")
# libraryInfo.find("a",)
print(libraryInfo.text)

html = urlopen("http://202.118.8.7:8991/F/VDGBD82QGS17QQ65QQMQTP59CRVJ13KG3BRQ9ML1A2X5UDHT92-31080?func=bor-info")
myInfo = bs(html, "html.parser")
# print(myInfo.text)

