import requests
api_url = "https://api.upbit.com/v1/market/all"

response = requests.get(api_url)

if response.status_code == 200:
    market_data = response.json()

    sorted_market_data = sorted(market_data, key=lambda x: x['market'])

    for market in sorted_market_data:
        print(
            f"Market: {market['market']}, Korean Name: {market['korean_name']}, English Name: {market['english_name']}")
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")
