import requests
from datetime import datetime


def get_current_price(market):
    api_url = f"https://api.upbit.com/v1/ticker?markets={market}"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if len(data) > 0:
            price = data[0].get('trade_price', None)
            timestamp = data[0].get('timestamp', None)
            if price is not None and timestamp is not None:
                timestamp = datetime.fromtimestamp(timestamp / 1000)
                return price, timestamp
            elif price is not None:
                return price, None
            else:
                return None, None
        else:
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"요청 중 에러 발생: {e}")
        return None, None


markets = ["KRW-BTC", "KRW-ETH", "KRW-XRP"]

for market in markets:
    price, timestamp = get_current_price(market)

    if price:
        if timestamp:
            print(f"현재 시간: {timestamp}")
        print(f"현재 금액은 1 {market.split('-')[1]}당 {price:,} 원입니다.")
    else:
        print(f"{market}에 대한 가격을 가져올 수 없습니다.")
