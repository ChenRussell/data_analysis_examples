from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import csv
import time

personInfoFile = open("../lib_info_postgraduate2/personalInfo.csv", 'w+', newline='', encoding='utf-8')
boringNumFile = open("../lib_info_postgraduate2/boringNum.csv", 'w+', newline='', encoding='utf-8')
presentBoringFile = open("../lib_info_postgraduate2/presentBoringInfo.csv", 'w+', newline='', encoding='utf-8')
historyBoringFile = open("../lib_info_postgraduate2/historyBoringInfo.csv", 'w+', newline='', encoding='utf-8')

writer = csv.writer(personInfoFile, delimiter=',')
writer2 = csv.writer(boringNumFile, delimiter=',')
writer3 = csv.writer(presentBoringFile, delimiter=',')
writer4 = csv.writer(historyBoringFile, delimiter=',')

firstRow = ["姓名", "学号", "地址"]
writer.writerow(firstRow)
writer2.writerow(["姓名", "学号", "外借", "借阅历史"])
writer3.writerow(["编号", "姓名", "学号", "作者", "书名", "出版年", "应还日期", "分馆", "索引号"])
writer4.writerow(["编号", "姓名", "学号", "作者", "书名", "出版年", "应还日期", "归还日期", "分馆"])

borId = 1670100
borVerification = 670100

# params = {'func': 'login-session',
#             'login_source': 'bor-info',
#             'bor_id': borId,
#             'bor_verification': borVerification,
#             'bor_library': 'NEU50'}
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
#            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#            "Accept-Language": "zh-CN,zh;q=0.8"}
#
# html = urlopen("http://202.118.8.7:8991/F/-?func=bor-info")
# loginPage = BeautifulSoup(html.read(), "html.parser")
# loginUrl = loginPage.find("form", {'name': 'form1'})
# print(loginUrl['action'])
# r = requests.post(loginUrl['action'], data=params, headers=headers)
# # print(r.content.decode('utf-8'))
#
# myInfo = BeautifulSoup(r.content.decode('utf-8'), "html.parser")
# baseInfo = myInfo.findAll("td")
# print(baseInfo[0].text)
# print(baseInfo[1].text.strip())
# print(baseInfo[2].text)
# print(baseInfo[3].text.strip())
# print(baseInfo[5].text.strip())
# print(baseInfo[7].text.strip())
# print(baseInfo[9].text.strip())
# nameCol = baseInfo[0].text.strip()
# name = baseInfo[1].text.strip()
# addCol = baseInfo[2].text.strip()
# address1 = baseInfo[3].text.strip()
# address2 = baseInfo[5].text.strip()
# address3 = baseInfo[7].text.strip()
# address4 = baseInfo[9].text.strip()
# addressArr = []
# j=3
# for i in range(4):
#     addressArr.append(baseInfo[j].text.strip())
#     j = j+2
# address = " ".join(addressArr)
# print(address)

def getPersonInfo():
    secondTable = myInfo.findAll("table")[1]
    # print(secondTable)
    global studentId
    studentId = secondTable.findAll("td")[5].text.strip()
    print(name+"  "+studentId)
    infoRow = [name, studentId, address]
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
    # print(presentUrl)
    # print(historyUrl)
    presentNum = hrefInfo[0].text.strip()
    historyNum = hrefInfo[1].text.strip()
    print(presentNum)
    print(historyNum)
    writer2.writerow([name, studentId, presentNum, historyNum])

def getPresentBoringInfo():
    presentBoringHtml = urlopen(presentUrl)
    presentBoringInfo = BeautifulSoup(presentBoringHtml, "html.parser")
    # print(presentBoringInfo)
    try:
        # print(len(presentBoringInfo.findAll("table")))
        # print(presentBoringInfo.findAll("table")[2].findAll("tr"))
        # print(len(presentBoringInfo.findAll("table")[2].findAll("tr")))
        for tr in presentBoringInfo.findAll("table")[2].findAll("tr")[1:]:
            td = tr.findAll("td")
            # print(len(td))
            writer3.writerow([td[0].text.strip(), name, studentId, td[2].text.strip(), td[3].text.strip(), td[4].text.strip(), td[5].text.strip(), td[7].text.strip(), td[8].text.strip()])
        # print(hrefInfo)
    except:
        print("无正在借阅记录！")

def getHistoryBoringInfo():
    historyBoringHtml = urlopen(historyUrl)
    historyBoringInfo = BeautifulSoup(historyBoringHtml, "html.parser")
    # print(historyBoringInfo)
    # print(len(historyBoringInfo.findAll("table")))
    try:
        # print(historyBoringInfo.findAll("table")[2])
        for tr in historyBoringInfo.findAll("table")[2].findAll("tr")[1:]:
            td = tr.findAll("td")
            writer4.writerow([td[0].text.strip(), name, studentId, td[1].text.strip(), td[2].text.strip(), td[3].text.strip(), td[4].text.strip(), td[6].text.strip(), td[9].text.strip()])
    except:
        print("无历史借阅记录！")

for i in range(1000):
    time.sleep(1.5)
    # print(borId)
    # print(borVerification)
    params = {'func': 'login-session',
              'login_source': 'bor-info',
              'bor_id': borId,
              'bor_verification': borVerification,
              'bor_library': 'NEU50'}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"}
    html = urlopen("http://202.118.8.7:8991/F/-?func=bor-info")
    loginPage = BeautifulSoup(html.read(), "html.parser")
    loginUrl = loginPage.find("form", {'name': 'form1'})
    # print(loginUrl['action'])
    r = requests.post(loginUrl['action'], data=params, headers=headers)
    borId += 1
    borVerification += 1
    myInfo = BeautifulSoup(r.content.decode('utf-8'), "html.parser")
    baseInfo = myInfo.findAll("td")
    try:
        nameCol = baseInfo[0].text.strip()                          #提示逾期未归还时此处会越界！
        name = baseInfo[1].text.strip()
        addCol = baseInfo[2].text.strip()
        addressArr = []
        j = 3
        for i in range(4):
            addressArr.append(baseInfo[j].text.strip())             #修改密码时此处会越界！
            j += 2
        address = " ".join(addressArr)
        print(address)
    except:
        print("用户已修改密码无法登陆，或提示有逾期未归还书籍！")
        continue
    getPersonInfo()
    getBoringNumInfo()
    getPresentBoringInfo()
    getHistoryBoringInfo()