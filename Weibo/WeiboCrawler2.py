from bs4 import BeautifulSoup
import urllib.request
with open('sources/1.1.txt','r') as file:

    soup = BeautifulSoup(file, "html.parser")
    i = 1
    title = '2014-03-14 了了一个愿望。 ​​​​​​'
    for link in soup.findAll('img'):
        href = link.get('src')
        href = str(href).replace('thumb180', 'large')


        full_name = title + str(i) + ".jpg"
        urllib.request.urlretrieve(href, full_name)
        print(full_name, href)
        i += 1
