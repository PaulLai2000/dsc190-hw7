import os
import pandas as pd

# 1. 讀取原始資料
df = pd.read_csv("data/raw/events.csv")

# 2. 移除任何欄位有缺失的列
df = df.dropna().copy()

# 3. 過濾合法的 event_type
VALID_TYPES = {"click", "login", "purchase", "scroll", "view"}
df = df[df["event_type"].isin(VALID_TYPES)].copy()

# 4. 篩選 duration_seconds 為正數 (> 0)
df = df[df["duration_seconds"] > 0].copy()

# 5. duration_seconds 轉為整數
df["duration_seconds"] = df["duration_seconds"].astype(int)

# 6. 時間戳記標準化為 ISO 8601 格式 YYYY-MM-DDTHH:MM:SS
df["timestamp"] = pd.to_datetime(df["timestamp"], format="mixed").dt.strftime("%Y-%m-%dT%H:%M:%S")

# 輸出結果
os.makedirs("data/clean", exist_ok=True)
df.to_csv("data/clean/events.csv", index=False)
