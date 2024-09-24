import requests
from bs4 import BeautifulSoup
import time
import csv
import logging
from datetime import datetime

# 로그 설정
logging.basicConfig(
    filename='naver_search_rank.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

# 네이버 검색어 순위를 가져오는 함수
def get_naver_search_rank():
    url = 'https://www.naver.com/'
    response = requests.get(url)
    if response.status_code != 200:
        logging.error(f"Failed to fetch Naver search data. Status Code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # 검색어 순위를 담고 있는 HTML 요소를 찾음
    rank_elements = soup.select('.ah_roll_area .ah_item .ah_k')
    if not rank_elements:
        logging.error("Failed to find search rank elements in the page.")
        return None

    ranks = [rank.text for rank in rank_elements][:10]  # 상위 10개의 검색어 추출
    logging.info("Successfully fetched Naver search rank data.")
    return ranks

# CSV 파일에 데이터 저장
def save_to_csv(data):
    filename = 'naver_search_rank.csv'
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([now] + data)

    logging.info("Data saved to CSV file.")

# 주기적으로 데이터를 수집하는 함수 (1분마다 실행)
def collect_data_periodically():
    while True:
        search_rank = get_naver_search_rank()
        if search_rank:
            save_to_csv(search_rank)
        time.sleep(60)  # 1분 대기

if __name__ == '__main__':
    logging.info("Started Naver search rank collection.")
    try:
        collect_data_periodically()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
