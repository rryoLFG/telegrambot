import requests
import time

# --- 各種設定 ---
BOT_TOKEN = '7742971479:AAGl68EsIdMm6X7XxlWrRCoSfbuW9bq-6Vw'
CHAT_ID = '5073454995'
THRESHOLD = 9000000  # 通知するBTC価格の閾値（円）

# --- BTC価格を取得 ---
def get_btc_price_jpy():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {'ids': 'bitcoin', 'vs_currencies': 'jpy'}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data['bitcoin']['jpy']
    except Exception as e:
        print("BTC価格の取得に失敗しました:", e)
        return None

# --- Telegramへ通知を送信 ---
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': message}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("✅ 通知送信成功！")
        else:
            print(f"❌ 通知送信失敗… ステータス: {response.status_code}")
    except Exception as e:
        print("通知中にエラー:", e)

# --- メインループ ---
while True:
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    price = get_btc_price_jpy()

    if price is not None:
        print(f"[{now}] BTC価格: ¥{price:,}")

        if price >= THRESHOLD:
            message = f"🚨【アラート】BTC価格は ¥{price:,} でございます！🌸（{now}）"
            send_telegram_message(message)

    time.sleep(60)  # 1分ごとに再実行
