import logging

# 로거 객체 생성
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)  # 전체 로거 레벨을 DEBUG로 설정

# 파일 핸들러 생성 (파일에 기록) - UTF-8 인코딩 추가 및 로그 레벨 DEBUG 설정
file_handler = logging.FileHandler('app.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)  # 파일에 모든 레벨 기록

# 콘솔 핸들러 생성 (콘솔에 출력)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # 콘솔에도 모든 레벨 기록

# 포맷터 설정
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 로거에 핸들러 추가
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 로그 작성
logger.debug('디버그 메시지')
logger.info('정보 메시지')
logger.warning('경고 메시지')
logger.error('에러 메시지')
logger.critical('치명적인 에러 메시지')
