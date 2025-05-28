
import pandas as pd

data = {
    "日付": ["2025-05-01", "2025-05-02"],
    "気温": [22.5, 23.0]
}

df = pd.DataFrame(data)
df.to_excel("気温データ.xlsx", index=False)

print("エクセルファイルを作成しました。")
