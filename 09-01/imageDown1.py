import os
import requests
import random
import string

def rnd_str(n=5):
  characters = string.ascii_letters + string.digits 
  return ''.join(random.choices(characters, k=n))

# 이미지 URL
url = "http://jeju-s.jje.hs.kr/boardCnts/fileDown.do?m=0203&s=jeju-s&fileSeq=8785962"


folder_name = "images"
script_directory = os.path.dirname(os.path.abspath(__file__)) # current_directory = os.getcwd()
folder_name = os.path.join(script_directory, "images")
if not os.path.exists( folder_name ):
  os.makedirs(folder_name)


response = requests.get(url)


file_path = os.path.join(folder_name, f"image-{rnd_str(5)}.jpg")

print("이미지 다운로드 시작!")
with open(file_path, "wb") as file:
   file.write(response.content)
print("이미지 다운로드 완료!")

