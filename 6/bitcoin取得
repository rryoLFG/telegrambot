import requests
from datetime import datetime
from openpyxl import load_workbook

# --- データ取得関数 ---
def fetch_data():
    # CoinGeckoでビットコイン価格取得
    btc_url = 'https://api.coingecko.com/api/v3/simple/price'
    btc_params = {
        'ids': 'bitcoin',
        'vs_currencies': 'jpy,usd'
    }
    btc_data = requests.get(btc_url, params=btc_params).json()
    btc_jpy = btc_data['bitcoin']['jpy']
    btc_usd = btc_data['bitcoin']['usd']

    # 為替（ドル円）取得：open.er-api.com に変更
    fx_url = "https://open.er-api.com/v6/latest/USD"
    fx_response = requests.get(fx_url)
    fx_response.raise_for_status()
    fx_data = fx_response.json()

    print("取得した為替データ:", fx_data)
    usd_jpy = fx_data["rates"]["JPY"]

    return btc_jpy, btc_usd, usd_jpy


# --- Excel書き込み関数 ---
def write_to_excel(file_path):
    btc_jpy, btc_usd, usd_jpy = fetch_data()
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H:%M:%S')

    # Excelファイルを読み込む
    wb = load_workbook(file_path)
    ws = wb.active

    # 次の行に追記
    next_row = ws.max_row + 1
    ws.cell(row=next_row, column=1, value=date_str)
    ws.cell(row=next_row, column=2, value=time_str)
    ws.cell(row=next_row, column=3, value=btc_jpy)
    ws.cell(row=next_row, column=4, value=btc_usd)
    ws.cell(row=next_row, column=5, value=usd_jpy)

    # 保存
    wb.save(file_path)

    # コンソール表示
    print(f"書き込み完了: {date_str} {time_str} BTC ¥{btc_jpy:,} / ${btc_usd:,} USD/JPY={usd_jpy:.2f}")

# --- 実行 ---
write_to_excel("bitcoin_log.xlsx")
