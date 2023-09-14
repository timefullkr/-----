
# pip install beautifulsoup4
from bs4 import BeautifulSoup

from urllib.request import urlopen


html = urlopen('http://jeju-s.jje.hs.kr/jeju-s/0203/board/18525/6475033')

soup = BeautifulSoup(html, 'html.parser')
items= soup.select('.fieldBox > dl > dd a')

print( "="*100)
print( items)
print( "="*100)
print( items[0].text)
print( items[0]["href"])
print( "="*100)
# for item in items:
   
#    print( item)
#    print( item.text)
#    print( "-"*100)
#    url=item["href"]
#    print( url)
#    imageUrl=f"http://jeju-s.jje.hs.kr{url}"
#    print( "이미지 url=" ,imageUrl)
#    print( "-"*100)
    
