import pandas as pd
from bs4 import BeautifulSoup

import requests

url= 'https://kolizhanka.com.ua/10-retseptiv-yak-prygotuvaty-smachnyj-sup/'

def parse(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

page = parse(url)
content = page.find('div', 'content-article')

def inside():
    i = 0
    for links in content.find_all('a', href=True):
        i += 1
        text = page.find('div', 'content-article').text
        words = len(text.split())
        img = len([tag.name for tag in page.find_all('img')])
        links = len([tag.name for tag in page.find_all('link')])
        tags = len([tag.name for tag in page.find_all()])
    print ("У тексті веб-сторінки знайдено")
    print ("Слів", words)
    print ("Зображень", img)
    print ("Тегів", tags)
    print ("Посилань", links)
print(inside())
