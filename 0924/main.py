import os
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# CSV 파일 경로 설정
csv_file = 'list.csv'

# 크롤링할 URL 설정
url = 'https://www.saramin.co.kr/zf_user/jobs/list/job-category?page=1&loc_mcd=105000&cat_kewd=82%2C2248%2C83%2C84%2C87%2C89&search_optional_item=n&search_done=y&panel_count=y&preview=y&isAjaxRequest=0&page_count=1000&sort=RL&type=job-category&is_param=1&isSearchResultEmpty=1&isSectionHome=0&searchParamCount=2#searchTitle'

# 헤더 추가
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 요청 및 응답 처리
response = requests.get(url, headers=headers)

# CSV 저장 함수
def save_csv_data(data):
    fieldnames = ['title', 'url', 'job', 'location', 'qualification', 'deadline']
    file_exists = os.path.exists(csv_file)
    with open(csv_file, mode='a' if file_exists else 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)\

# 데이터 추출 및 저장
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    list_items = soup.find_all('div', class_='list_item')

    for item in list_items:
        # 추출부분
        company_nm_div = item.find('div', class_='col company_nm')
        title_tag = company_nm_div.find('a', class_='str_tit') if company_nm_div else None
        title = title_tag.get_text(strip=True) if title_tag else 'No title'

        notification_info_div = item.find('div', class_='col notification_info')
        url_tag = notification_info_div.find('a', class_='str_tit') if notification_info_div else None
        url = 'https://www.saramin.co.kr' + url_tag['href'] if url_tag and 'href' in url_tag.attrs else 'No link'

        job_sector = item.find('span', class_='job_sector')
        job = ', '.join([child.get_text(strip=True) for child in job_sector.find_all()]) if job_sector else 'No job info'

        location_tag = item.find('p', class_='work_place')
        location = location_tag.get_text(strip=True) if location_tag else 'No location info'

        career_tag = item.find('p', class_='career')
        education_tag = item.find('p', class_='education')
        qualification = (career_tag.get_text(strip=True) if career_tag else 'No career info') + ", " + (education_tag.get_text(strip=True) if education_tag else 'No education info')

        support_detail = item.find('p', class_='support_detail')
        deadline_tag = support_detail.find('span', class_='date') if support_detail else None
        deadline = deadline_tag.get_text(strip=True) if deadline_tag else 'No deadline info'

        # 선언부분
        save_csv_data({
            'title': title,
            'url': url,
            'job': job,
            'location': location,
            'qualification': qualification,
            'deadline': deadline
        })

    print("파싱 완료")
else:
    print(f"Failed to fetch the webpage. HTTP Status: {response.status_code}")
