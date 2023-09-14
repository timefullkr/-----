# pip install beautifulsoup4
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://jeju-s.jje.hs.kr/jeju-s/0203/board/18525/6475033')

soup = BeautifulSoup(html, 'html.parser')

items= soup.select('.fieldBox > dl > dd a')

for item in items:
   url=item["href"]
   
   imageUrl=f"http://jeju-s.jje.hs.kr/{url}"
   # ret=imageDownFun.imageDown(imageUrl)
   print( imageUrl )
    
