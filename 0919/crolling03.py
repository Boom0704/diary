import requests
from bs4 import BeautifulSoup
import os
import uuid

# 크롤링할 URL 설정 (Cine21 박스오피스 페이지)
url = "http://m.cine21.com/movie/boxoffice"

# 헤더에 User-Agent 추가 (브라우저로부터 온 요청처럼 보이게 함)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 웹 페이지 HTML 소스를 가져옴
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"Failed to retrieve page: {response.status_code}")
else:
    # HTML을 파싱하여 이미지 태그를 찾아냄
    soup = BeautifulSoup(response.text, 'html.parser')

    # 이미지 폴더를 생성 (폴더가 없을 경우)
    if not os.path.exists('cine21_posters02'):
        os.makedirs('cine21_posters02')

    # 모든 이미지 태그를 검색 (이미지 태그가 <img>로 되어있음)
    image_tags = soup.find_all('img')

    # 각 이미지 URL을 반복하여 이미지를 저장
    for i, img_tag in enumerate(image_tags):
        img_url = img_tag.get('src')

        # URL에 프로토콜이 없으면 추가 (이미지 URL이 "//"로 시작할 수 있음)
        if img_url.startswith('//'):
            img_url = 'http:' + img_url

        # 이미지 다운로드 및 저장
        try:
            img_data = requests.get(img_url).content

            # 유니크한 파일 이름 생성
            unique_filename = str(uuid.uuid4()) + '.jpg'

            # 파일 저장 (cine21_posters02 폴더 내에 저장)
            with open(f'./cine21_posters02/{unique_filename}', 'wb') as handler:
                handler.write(img_data)

            print(f"Image {i+1} saved as {unique_filename}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download image {i+1}: {e}")

    print(f"총 {len(image_tags)}개의 이미지를 저장했습니다.")

