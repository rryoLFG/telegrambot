from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "価格ログ"

# ヘッダーを追加
headers = ["日付", "時刻", "BTC価格(JPY)", "BTC価格(USD)", "ドル円レート"]
for col, header in enumerate(headers, start=1):
    ws.cell(row=1, column=col, value=header)

# 保存
wb.save("bitcoin_log.xlsx")
print("ファイル作成完了：bitcoin_log.xlsx")
