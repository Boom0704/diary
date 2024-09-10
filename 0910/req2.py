import requests
from datetime import datetime


def get_current_price():
    api_url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"
    try:
        response = requests.get(api_url, timeout=10)  # timeout 설정으로 요청이 너무 오래 걸리지 않게 설정
        response.raise_for_status()  # HTTP 에러가 있는 경우 예외 발생

        data = response.json()

        if len(data) > 0:  # 데이터가 비어있지 않은지 확인
            price = data[0].get('trade_price', None)  # 'trade_price' 키가 있는지 확인
            timestamp = data[0].get('timestamp', None)  # 'timestamp' 키가 있는지 확인
            if price is not None and timestamp is not None:
                timestamp = datetime.fromtimestamp(timestamp / 1000)  # Unix 타임스탬프를 변환
                return price, timestamp
            elif price is not None:  # 시간은 없지만 가격이 있는 경우
                return price, None
            else:
                return None, None  # 가격이 없는 경우
        else:
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"요청 중 에러 발생: {e}")
        return None, None


price, timestamp = get_current_price()

if price:
    if timestamp:
        print(f"현재 시간: {timestamp}")
    print(f"현재 금액은 1 비트코인당 {price:,} 원입니다.")
else:
    print("가격을 가져올 수 없습니다.")
