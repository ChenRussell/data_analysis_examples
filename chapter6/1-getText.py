from urllib.request import urlopen

textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
# print(textPage.read())
# print(type(textPage.read()))
print(str(textPage.read(), 'utf-8'))    #会换行
