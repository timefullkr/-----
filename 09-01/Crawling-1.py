# pip install requests
# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

# naver.com 웹 페이지를 가져옴

from urllib.request import urlopen
html = urlopen('https://www.naver.com')
soup = BeautifulSoup(html, 'html.parser')
title = soup.find('title')
print(f'Title of naver.com1-1: {title}')

title = soup.find('title').get_text()
print(f'Title of naver.com1-2: {title}')

title = soup.select("head > title")
print(f'Title of naver.com2-1: {title}')

title = soup.select("head > title")[0].text
print(f'Title of naver.com2-2: {title}')

