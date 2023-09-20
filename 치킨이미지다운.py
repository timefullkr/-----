from bs4 import BeautifulSoup
from selenium import webdriver
import time
import imageDownFun

driver = webdriver.Chrome()

# 웹 페이지 로드
driver.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query=chicken+&oquery=chicken+image&tqi=idqJSwprvTosshsevlVssssstpo-235214")


time.sleep(5)

# 스크롤을 사이드바 밑까지 내림
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# 추가로 로딩되는 요소를 기다림
time.sleep(5)


html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')


items= soup.select('.photo_bx > .thumb > a img')

for item in items:
   url=item["src"]
   if  "jpg" in url or "png" in url :
        print( url )
        ret=imageDownFun.imageDown(url)
        print(ret)

driver.quit()