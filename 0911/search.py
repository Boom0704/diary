import os
import fnmatch

def find_files(directory, pattern):
    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            # 패턴이 일치하거나 패턴이 파일명에 포함되어 있으면 추가
            if fnmatch.fnmatch(filename.lower(), pattern.lower()) or pattern.lower() in filename.lower():
                matches.append(os.path.join(root, filename))
    return matches

if __name__ == '__main__':
    # 사용자 입력을 받음
    search_directory = input("파일을 찾을 경로를 입력하세요 (예: C://Users//username//Desktop): ").strip()
    search_pattern = input("찾을 파일 이름 또는 패턴을 입력하세요 (예: java1.java 또는 *.java): ").strip()

    # 파일을 찾음
    found_files = find_files(search_directory, search_pattern)

    # 결과 출력
    if found_files:
        print(f"'{search_pattern}' 패턴과 일치하는 파일을 찾았습니다:")
        for file in found_files:
            print(file)
    else:
        print(f"'{search_pattern}' 패턴과 일치하는 파일을 찾을 수 없습니다.")
