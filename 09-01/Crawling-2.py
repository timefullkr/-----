# pip install requests
# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
import imageDown2

# naver.com 웹 페이지를 가져옴

from urllib.request import urlopen


html = urlopen('http://jeju-s.jje.hs.kr/jeju-s/0203/board/18525/6475033')

soup = BeautifulSoup(html, 'html.parser')
items= soup.select('.fieldBox > dl > dd a')

print( "="*100)
print( items)
print( "="*100)
print( items[0].text)
print( "="*100)
for item in items:
   
   print( item)
   print( item.get_text())
   print( "-"*100)
   url=item["href"]
   print( url)
   print( "이미지 url=" ,f"http://jeju-s.jje.hs.kr{url}")
   print( "-"*100)
    
