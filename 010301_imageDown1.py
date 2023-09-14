import requests

image_url = "http://jeju-s.jje.hs.kr/upload/sysImg/jeju-s/SysImg_201706270515413650.png"

response = requests.get(image_url)

with open("downloaded_image.png", "wb") as f:
       f.write(response.content)

# 파일명  
#  url 파일명, 임의 파일명