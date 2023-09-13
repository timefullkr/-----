# pip install requests
# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
import imageDown2
from urllib.request import urlopen

html = urlopen('http://jeju-s.jje.hs.kr/jeju-s/0203/board/18525/6475033')

soup = BeautifulSoup(html, 'html.parser')
items= soup.select('.fieldBox > dl > dd a')
for item in items:
   url=item["href"]
   
   imageUrl=f"http://jeju-s.jje.hs.kr/{url}"
   ret=imageDown2.imageDown(imageUrl)
   print(ret )
    
