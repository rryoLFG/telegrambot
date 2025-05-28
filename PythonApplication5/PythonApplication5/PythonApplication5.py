
import requests

def get_btc_price_jpy():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'jpy'
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        price = data['bitcoin']['jpy']
        print(f"現在のビットコイン価格（JPY）: ¥{price:,}")
    except requests.exceptions.RequestException as e:
        print(f"価格取得中にエラーが発生しました: {e}")

# 実行
get_btc_price_jpy()
