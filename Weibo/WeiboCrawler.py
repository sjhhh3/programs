from bs4 import BeautifulSoup
import urllib.request
with open('sources/13.txt','r') as file:

    soup = BeautifulSoup(file, "html.parser")
    #print(soup)
    titlelist = []
    hreflist = []
    datelist = []
    dic = {}
    lentitle = 0
    lenhref = 0
    for link in soup.findAll('span','ctt'):
        #print(link)
        while str(link).find('<a') != -1:
            loc = str(link).find('<a')
            end = str(link)[loc:].find('>')+loc
            link = str(link)[:loc] + str(link)[end+1:]
            link = link.replace('</a>','')

            continue
        loc2 = str(link).find('http://t.cn/')
        end2 = str(link)[loc2:].find(' ') + loc2
        link = str(link)[:loc2] + str(link)[end2 + 1:]
        link = link[18:-9]
        delete = '?:*"/\<>|'
        for char in delete:
            link = link.replace(char,'')


        #title = link.string
        titlelist.append(link)
        lentitle += 1
    #print(titlelist)
    #print(lentitle)

    for link in soup.findAll('span','ct'):
        loc3 = str(link).find('<a')
        end3 = str(link)[loc3:].find('>')+loc3
        link = str(link)[:loc3] + str(link)[end3+1:]
        link = link.replace('</a>','')
        date = link[17:27]
        datelist.append(date)

    for link in soup.findAll('img'):
        href = link.get('src')
        href = str(href).replace('wap180', 'large')
        hreflist.append(href)
        lenhref += 1
    hreflist = hreflist[:-1]
    #
    # # # print(hreflist)
    # # # print(lenhref)
    # #
    i = 0
    while i < lentitle:
        dic[datelist[i]+' '+titlelist[i]] = hreflist[i]
        i += 1
    for key in dic:
        full_name = key + ".jpg"
        urllib.request.urlretrieve(dic[key], full_name)
        print(full_name, dic[key])
