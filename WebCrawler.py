import requests
from bs4 import BeautifulSoup

#fw = open('dzy.txt','w')
def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.daizhiyong.top/?cat=8&paged='+ str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a'):
            href = link.get('href')
            title = link.string
            if href[-5] == 'p':
                #fw.write(href+'\n')
                #fw.write(title+'\n')
                print(href)
                print(title)

        page += 1

# def get_single_data(item_url):
#     source_code = requests.get(item_url)
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text)
#     for item_date in soup.findAll('p'):
#         item = str(item_date)
#         loc = item.find('Post')
#         break
#     date = item[loc+20:loc+30]
#     fw.write(date+'\n')

trade_spider(1)
