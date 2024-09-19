

import requests
from bs4 import BeautifulSoup
import re
import os
import urllib.request as req

from urllib3 import request

req.urlretrieve('https://image.cine21.com/resize/cine21/poster/2014/0721/39921_53cca0ce20300_main_poster01[F230,329].jpg','test.jpg')

image_path = './img'
url = "http://m.cine21.com/movie/boxoffice/history"
res = requests.get(url)

if not os.path.exists(image_path):
    os.mkdir(image_path)

soup = BeautifulSoup(res.content, "html.parser")
div = soup.select_one('.lst_ranking_area')
img = div.find_all('img')

for i, img in enumerate(img):
    print(i, img['src'])
    req.urlretrieve(img['src'], os.path.join(image_path, str(i) + ".jpg"))

