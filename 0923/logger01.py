import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import time
import logging

# 로그 설정
logging.basicConfig(
    filename='kospi_list_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

# 지난 3개의 결과를 저장할 리스트
previous_results = []

# 타이머 상태 변수
timer_seconds = 10  # 10초 타이머 설정
current_time = timer_seconds


# 네이버 금융 코스피 종목 리스트 크롤링 함수
def fetch_kospi_list():
    url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0'  # 네이버 코스피 종목 URL
    response = requests.get(url)

    if response.status_code != 200:
        logging.error(f"Failed to fetch kospi data. Status Code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # 종목 데이터를 추출하는 부분 (표에 있는 종목 이름 추출)
    table = soup.find('table', class_='type_2')
    rows = table.find_all('tr')[2:]  # 헤더와 빈 줄 제외

    data = []
    for row in rows:
        columns = row.find_all('td')
        if len(columns) > 1:
            code = columns[1].get_text(strip=True)  # 종목 코드
            name = columns[2].get_text(strip=True)  # 종목 이름
            price = columns[3].get_text(strip=True)  # 종가
            data.append((code, name, price))

    logging.info("Successfully fetched Kospi data.")
    return data


# 데이터 갱신 및 테이블 업데이트
def show_table_data():
    global previous_results

    data = fetch_kospi_list()

    if not data:
        status_label.config(text="데이터를 가져오지 못했습니다.")
        return

    # 최신 데이터 Treeview에 업데이트
    tree.delete(*tree.get_children())  # 이전 데이터 삭제
    for row in data:
        tree.insert('', 'end', values=row)

    # 지난 3개의 결과 업데이트
    if len(previous_results) >= 3:
        previous_results.pop(0)  # 가장 오래된 결과 제거
    previous_results.append(data)

    # 이전 결과 업데이트
    update_previous_results_view()

    status_label.config(text="데이터 가져오기 완료")
    logging.info("Data successfully updated and displayed.")


# 지난 3개의 결과를 업데이트하는 함수
def update_previous_results_view():
    previous_tree.delete(*previous_tree.get_children())  # 이전 결과 삭제
    for idx, result in enumerate(previous_results):
        for row in result:
            previous_tree.insert('', 'end', values=row)


# 10초 타이머 실행 함수
def update_timer():
    global current_time

    if current_time > 0:
        timer_label.config(text=f"다음 데이터 갱신까지: {current_time} 초")
        current_time -= 1
        root.after(1000, update_timer)  # 1초마다 갱신
    else:
        current_time = timer_seconds
        show_table_data()  # 데이터 갱신
        update_timer()  # 타이머 재시작


# Tkinter 기본 설정
root = tk.Tk()
root.title("코스피 데이터 실시간 갱신")

# 상태 표시 라벨
status_label = tk.Label(root, text="데이터를 가져오려면 버튼을 클릭하세요.", font=("Arial", 12))
status_label.pack(pady=10)

# 타이머 라벨
timer_label = tk.Label(root, text="다음 데이터 갱신까지: 10 초", font=("Arial", 12), fg="blue")
timer_label.pack(pady=10)

# Treeview 위젯 (현재 데이터)
columns = ('종목코드', '종목명', '종가')  # 실제 열 이름 설정
tree = ttk.Treeview(root, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(pady=20)

# 지난 3개의 결과를 보여줄 Treeview
previous_tree_label = tk.Label(root, text="지난 3개의 결과:", font=("Arial", 12))
previous_tree_label.pack(pady=5)

previous_tree = ttk.Treeview(root, columns=columns, show='headings')

for col in columns:
    previous_tree.heading(col, text=col)
    previous_tree.column(col, width=100)

previous_tree.pack(pady=20)

# 데이터 가져오기 버튼
fetch_button = tk.Button(root, text="데이터 가져오기", command=show_table_data, font=("Arial", 12))
fetch_button.pack(pady=10)

# 타이머 시작
update_timer()

# Tkinter 이벤트 루프 시작
root.mainloop()
