from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import csv

personInfoFile = open("../lib_info/personalInfo.csv", 'w+', newline='', encoding='utf-8')
boringNumFile = open("../lib_info/boringNum.csv", 'w+', newline='', encoding='utf-8')
presentBoringFile = open("../lib_info/presentBoringInfo.csv", 'w+', newline='', encoding='utf-8')
historyBoringFile = open("../lib_info/historyBoringInfo.csv", 'w+', newline='', encoding='utf-8')
borId = 1670766
borVerification = 670766

params = {'func': 'login-session',
            'login_source': 'bor-info',
            'bor_id': borId,
            'bor_verification': borVerification,
            'bor_library': 'NEU50'}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Language": "zh-CN,zh;q=0.8"}

html = urlopen("http://202.118.8.7:8991/F/-?func=bor-info")
loginPage = BeautifulSoup(html.read(), "html.parser")
loginUrl = loginPage.find("form", {'name': 'form1'})
print(loginUrl['action'])
# r = requests.post(loginUrl['action'], data=params, headers=headers)
r = requests.post("http://202.118.8.7:8991/F/ITAXX6N1JUY1EBG95A7AIUMHD2XMB4N8S3P2X74FKP1HYXRUAM-27114", data=params, headers=headers)
# print(r.content.decode('utf-8'))

myInfo = BeautifulSoup(r.content.decode('utf-8'), "html.parser")
baseInfo = myInfo.findAll("td")
print(baseInfo[0].text)
print(baseInfo[1].text.strip())
print(baseInfo[2].text)
print(baseInfo[3].text.strip())
print(baseInfo[5].text.strip())
print(baseInfo[7].text.strip())
print(baseInfo[9].text.strip())
nameCol = baseInfo[0].text.strip()
name = baseInfo[1].text.strip()
addCol = baseInfo[2].text.strip()
address1 = baseInfo[3].text.strip()
address2 = baseInfo[5].text.strip()
address3 = baseInfo[7].text.strip()
address4 = baseInfo[9].text.strip()
addressArr = []
j=3
for i in range(4):
    addressArr.append(baseInfo[j].text.strip())
    j = j+2
address = " ".join(addressArr)
print(address)

def getPersonInfo():
    secondTable = myInfo.findAll("table")[1]
    # print(secondTable)
    global studentId
    studentId = secondTable.findAll("td")[5].text.strip()
    print(studentId)
    writer = csv.writer(personInfoFile, delimiter=',')
    firstRow = [nameCol, "学号", addCol]
    infoRow = [name, studentId, address]
    writer.writerow(firstRow)
    writer.writerow(infoRow)
    # baseInfo = myInfo.find("table", {"class", "indent1"}).findAll("td")
    # print(baseInfo)

# print(myInfo.text)
def getBoringNumInfo():
    thirdTable = myInfo.find("table", {"class", "indent1"})
    hrefInfo = thirdTable.findAll("a")
    # for tagA in hrefInfo:
        # print(tagA['href'].split('\'')[1])
    global presentUrl, historyUrl
    presentUrl = hrefInfo[0]['href'].split('\'')[1]
    historyUrl = hrefInfo[1]['href'].split('\'')[1]
    print(presentUrl)
    print(historyUrl)
    presentNum = hrefInfo[0].text.strip()
    historyNum = hrefInfo[1].text.strip()
    print(presentNum)
    print(historyNum)
    writer2 = csv.writer(boringNumFile)
    writer2.writerow([nameCol, "学号", "外借", "借阅历史"])
    writer2.writerow([name, studentId, presentNum, historyNum])

def getPresentBoringInfo():
    presentBoringHtml = urlopen(presentUrl)
    presentBoringInfo = BeautifulSoup(presentBoringHtml, "html.parser")
    # print(presentBoringInfo)
    print(len(presentBoringInfo.findAll("table")))
    # print(presentBoringInfo.findAll("table")[2].findAll("tr"))
    # print(len(presentBoringInfo.findAll("table")[2].findAll("tr")))
    writer3 = csv.writer(presentBoringFile)
    writer3.writerow(["编号", nameCol, "学号", "作者", "书名", "出版年", "应还日期", "分馆", "索引号"])
    for tr in presentBoringInfo.findAll("table")[2].findAll("tr")[1:]:
        td = tr.findAll("td")
        print(len(td))
        writer3.writerow([td[0].text.strip(), name, studentId, td[2].text.strip(), td[3].text.strip(), td[4].text.strip(), td[5].text.strip(), td[7].text.strip(), td[8].text.strip()])
    # print(hrefInfo)

def getHistoryBoringInfo():
    historyBoringHtml = urlopen(historyUrl)
    historyBoringInfo = BeautifulSoup(historyBoringHtml, "html.parser")
    # print(historyBoringInfo)
    # print(len(historyBoringInfo.findAll("table")))
    print(historyBoringInfo.findAll("table")[2])
    writer4 = csv.writer(historyBoringFile)
    writer4.writerow(["编号", "作者", "书名", "出版年", "应还日期", "归还日期", "分馆"])
    for tr in historyBoringInfo.findAll("table")[2].findAll("tr")[1:]:
        td = tr.findAll("td")
        writer4.writerow([td[0].text.strip(), td[1].text.strip(), td[2].text.strip(), td[3].text.strip(), td[4].text.strip(), td[6].text.strip(), td[9].text.strip()])
getPersonInfo()
getBoringNumInfo()
getPresentBoringInfo()
getHistoryBoringInfo()

