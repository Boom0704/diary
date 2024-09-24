import csv
from db import save_to_db

# CSV 파일을 읽어오는 함수
def read_csv(file_name):
    data = []
    with open(file_name, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        columns = next(csv_reader)  # 첫 번째 줄을 컬럼 이름으로 사용
        for row in csv_reader:
            data.append(row)  # 데이터를 리스트로 저장
    return columns, data

# 메인 실행 함수
def main():
    csv_file_name = 'kospi_list.csv'  # 읽을 CSV 파일 이름

    # CSV 데이터를 읽고 데이터베이스에 저장
    columns, data = read_csv(csv_file_name)
    save_to_db(csv_file_name, columns, data)

if __name__ == "__main__":
    main()
