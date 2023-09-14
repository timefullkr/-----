import os
import requests
import random
import string

def rnd_str(n=5):
  characters = string.ascii_letters + string.digits 
  return ''.join(random.choices(characters, k=n))


image_url  ="http://jeju-s.jje.hs.kr/upload/sysImg/jeju-s/SysImg_201706270515413650.png"

folder_name = "images"
if not os.path.exists( folder_name ):
  os.makedirs(folder_name)

response = requests.get(image_url )

file_name = f"image-{rnd_str()}.jpg"
file_path = os.path.join(folder_name, file_name)

print("이미지 다운로드 시작 >> ",file_name, end="")

with open(file_path, "wb") as file:
   file.write(response.content)
print("  >>  완료!")
