import requests
from bs4 import BeautifulSoup
import os

# 크롤링할 URL 설정 (IMDb 인기 영화 페이지 예시)
url = 'https://www.imdb.com/chart/moviemeter/'

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
    if not os.path.exists('posters'):
        os.makedirs('posters')

    # 포스터 이미지 URL을 저장할 리스트
    image_urls = []

    # 모든 이미지 태그를 검색 (IMDb는 포스터 이미지가 <img> 태그 안에 있음)
    for img_tag in soup.find_all('img'):
        img_url = img_tag.get('src')

        # URL에 프로토콜이 없으면 추가
        if img_url and img_url.startswith('//'):
            img_url = 'https:' + img_url

        # img_url이 None이 아닌지 확인하고, URL을 저장
        if img_url:
            image_urls.append(img_url)

    # 각 이미지 URL을 반복하여 이미지를 저장
    for i, img_url in enumerate(image_urls):
        # 이미지 다운로드
        try:
            img_data = requests.get(img_url).content

            # 파일 저장 (posters 폴더 내에 저장, 파일 이름은 index로 구분)
            with open(f'./posters/poster_{i+1}.jpg', 'wb') as handler:
                handler.write(img_data)

            print(f"Image {i+1} saved.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download image {i+1}: {e}")

    print(f"총 {len(image_urls)}개의 이미지를 저장했습니다.")
