import os
import requests
import random
import string

def rnd_str(n=5):
  # 이미지 파일 명을 만들기 위한  임의 숫자 발생
  characters = string.ascii_letters + string.digits 
  return ''.join(random.choices(characters, k=n))

def imageDown(url):
    # 이미지 URL
    #url = "http://jeju-s.jje.hs.kr/boardCnts/fileDown.do?m=0203&s=jeju-s&fileSeq=8785962"
    # "images" 폴더가 없으면 생성
    folder_name = "images"
    script_directory = os.path.dirname(os.path.abspath(__file__)) # current_directory = os.getcwd()
    folder_name = os.path.join(script_directory, "images")
    
    if not os.path.exists(folder_name):os.makedirs(folder_name)

    # URL에서 이미지의 정보를 가저온다.
    response = requests.get(url)
    fileName=f"image-{rnd_str(5)}.jpg"
    
    file_path = os.path.join(folder_name, fileName )

   # URL에서 이미지를 다운로드합니다.
    with open(file_path, "wb") as file:
      file.write(response.content)
   
    return fileName
    