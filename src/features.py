import os
import pandas as pd

df = pd.read_csv("data/transformed/events.csv")

# 新增 duration_minutes 與 weekday
df["duration_minutes"] = df["duration_seconds"] / 60.0
df["weekday"] = pd.to_datetime(df["date"]).dt.day_name()

os.makedirs("data/features", exist_ok=True)
df.to_csv("data/features/events.csv", index=False)
