import os
import requests
import random
import string

def rnd_str(n=5):
  # 이미지 파일 명을 만들기 위한  임의 문자 발생
  return ''.join(random.choices(string.digits, k=n))

# 이미지 URL
url = "http://jeju-s.jje.hs.kr/boardCnts/fileDown.do?m=0203&s=jeju-s&fileSeq=8785962"

# "images" 폴더가 없으면 생성
folder_name = "images"
if not os.path.exists(folder_name):os.makedirs(folder_name)
# URL에서 이미지를 다운로드합니다.
response = requests.get(url)
# "images" 폴더 안에 이미지를 저장합니다.
file_path = os.path.join(folder_name, f"image-{rnd_str(5)}.jpg")

print("이미지 다운로드 시작!")
with open(file_path, "wb") as file:
   file.write(response.content)
print("이미지 다운로드 완료!")

# 심풀하고 AI 활용한 학교 홈 만들기