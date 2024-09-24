import cx_Oracle

def connect_to_db():
    try:
        # 오라클 데이터베이스에 연결
        connection = cx_Oracle.connect("member", "member", "localhost/xe")
        return connection
    except cx_Oracle.DatabaseError as e:
        print(f"데이터베이스 연결 실패: {e}")
        return None

def fetch_data_from_table(table_name):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            data = cursor.fetchall()
            cursor.close()
            return data
        except cx_Oracle.DatabaseError as e:
            print(f"데이터 가져오기 실패: {e}")
            return []
        finally:
            conn.close()
    else:
        return []
