import tkinter as tk
from tkinter import ttk
from db_connection import fetch_data_from_table


def show_table_data():
    data = fetch_data_from_table("kospi_list")  # TB_USER 테이블 데이터 가져오기

    if not data:
        status_label.config(text="데이터를 가져오지 못했습니다.")
        return

    # 데이터 출력 (Treeview 사용)
    for i, row in enumerate(data):
        tree.insert('', 'end', values=row)

    status_label.config(text="데이터 가져오기 완료")


# Tkinter 기본 설정
root = tk.Tk()
root.title("TB_USER 테이블 데이터")

# 상태 표시 라벨
status_label = tk.Label(root, text="데이터를 가져오려면 버튼을 클릭하세요.", font=("Arial", 12))
status_label.pack(pady=10)

# Treeview 위젯 (테이블 형태로 데이터를 표시하기 위해)
columns = ('Column1', 'Column2', 'Column3', "Column4", "Column5", 'Column6')  # 실제 테이블에 맞게 열 이름 설정
tree = ttk.Treeview(root, columns=columns, show='headings')

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(pady=20)

# 데이터 가져오기 버튼
fetch_button = tk.Button(root, text="데이터 가져오기", command=show_table_data, font=("Arial", 12))
fetch_button.pack(pady=10)

# Tkinter 이벤트 루프 시작
root.mainloop()
