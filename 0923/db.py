import cx_Oracle
import os


# 데이터베이스 연결 함수
def connect_to_db():
    user = 'member'
    password = 'member'
    dsn = 'localhost/xe'
    connection = cx_Oracle.connect(user, password, dsn)
    return connection


# CSV 파일의 첫 줄을 컬럼 이름으로 사용하여 테이블 생성 및 데이터 저장
def save_to_db(csv_file_name, columns, data):
    connection = connect_to_db()
    cursor = connection.cursor()

    # 파일 이름에서 확장자를 제거하여 테이블 이름으로 사용
    table_name = os.path.splitext(csv_file_name)[0].upper()

    # 컬럼 이름을 조합하여 테이블 생성 쿼리 생성
    column_definitions = ', '.join([f"{col} VARCHAR2(100)" for col in columns])

    # 테이블이 이미 존재하는 경우 삭제
    drop_table_query = f"DROP TABLE {table_name} PURGE"

    try:
        # 테이블 삭제 시도 (존재하지 않으면 무시)
        cursor.execute(drop_table_query)
        print(f"Table {table_name} dropped successfully.")
    except cx_Oracle.DatabaseError as e:
        print(f"Warning: Table {table_name} might not exist, skipping drop.")

    # 테이블 생성
    create_table_query = f"CREATE TABLE {table_name} ({column_definitions})"
    try:
        cursor.execute(create_table_query)
        print(f"Table {table_name} created successfully.")
    except cx_Oracle.DatabaseError as e:
        print(f"Error creating table: {e}")

    # 데이터 삽입 쿼리 생성
    placeholders = ', '.join([f":{i + 1}" for i in range(len(columns))])
    insert_query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"

    try:
        # 데이터 삽입
        cursor.executemany(insert_query, data)
        connection.commit()
        print(f"Data saved to table {table_name} successfully.")
    except cx_Oracle.DatabaseError as e:
        print(f"Error inserting data: {e}")
        connection.rollback()

    cursor.close()
    connection.close()
