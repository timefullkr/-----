# pip install requests, # pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('https://weather.naver.com/today/14110120?cpName=KMA')

soup = BeautifulSoup(html, 'html.parser')

list = soup.select('.summary')


print("="*100)
print(list)
print("-"*100)

txt = list[0].text
print(txt)

print("="*100)

# 한 줄에 출력 
