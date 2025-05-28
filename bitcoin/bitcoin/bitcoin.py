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
        print(f"���݂̃r�b�g�R�C�����i�iJPY�j: ?{price:,}")
    except requests.exceptions.RequestException as e:
        print(f"�G���[���������܂���: {e}")

get_btc_price_jpy()

