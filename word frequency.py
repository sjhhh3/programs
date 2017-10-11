
import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code,"html.parser")
    for post_text in soup.findAll('p'):
        content = post_text.string
        words = str(content).lower().split()
        for each_word in words:
            #print(each_word)
            word_list.append(each_word)
    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        word = word.replace("none", "")
        numbers = "1234567890"
        for i in range(0,len(numbers)):
            word = word.replace(numbers[i],"")
        if len(word)>0:
            clean_word_list.append(word)
    creat_dictionary(clean_word_list)

def creat_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key,value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key,value)

start('https://store.nike.com/us/en_us/pw/mens-basketball-shoes/7puZ8r1Zoi3')
