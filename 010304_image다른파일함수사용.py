import os
import requests
import random
import string
import imageDownFun


url_1 ="http://jeju-s.jje.hs.kr/upload/sysImg/jeju-s/SysImg_201706270515413650.png"

ret=imageDownFun.imageDown(url_1)

print(ret )
