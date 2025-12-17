import pandas as pd
import numpy as np

df = pd.read_csv("csv_1.csv")

np.random.seed(42)

risk = (
    0.02 * (df["Age"] - 20) +
    0.04 * (df["BMI"] - 22) +
    0.015 * (df["BloodPressure"] - 120) +
    0.02 * (df["Glucose"] - 90) +
    0.01 * (df["Cholesterol"] - 180) +
    0.15 * (df["Smoking"] == "Yes").astype(int) -
    0.05 * df["Exercise_per_week"]
)

# 정규화
risk = (risk - risk.min()) / (risk.max() - risk.min())

df["Disease_Prob"] = np.clip(risk, 0, 1)

df1 = df.copy()

# 아주 약한 노이즈만
df1["Disease_Prob"] += np.random.normal(0, 0.02, len(df1))
df1["Disease_Prob"] = np.clip(df1["Disease_Prob"], 0, 1)

df1.to_csv("csv1.csv", index=False)


df2 = df1.copy()

# 8% 행에 이상치 주입
idx = df2.sample(frac=0.08, random_state=1).index

df2.loc[idx, "Disease_Prob"] += np.random.normal(0, 0.25, len(idx))
df2["Disease_Prob"] = np.clip(df2["Disease_Prob"], 0, 1)

df2.to_csv("csv2.csv", index=False)

df3 = df1.copy()  # 1번 CSV 기반

np.random.seed(42)

# 1. 일부 이상치 주입 (약 15% 행)
idx_outlier = df3.sample(frac=0.15, random_state=2).index
df3.loc[idx_outlier, "Disease_Prob"] += np.random.normal(0, 0.4, len(idx_outlier))

# 2. 일부 결측치 삽입 (약 10% 행)
for col in ["Glucose", "BloodPressure", "BMI"]:
    idx_nan = df3.sample(frac=0.1, random_state=np.random.randint(100)).index
    df3.loc[idx_nan, col] = np.nan

# 3. 일부 비상식적 값 삽입
df3.loc[df3.sample(frac=0.05, random_state=3).index, "Cholesterol"] *= 3
df3.loc[df3.sample(frac=0.05, random_state=4).index, "BMI"] = df3["BMI"] * 0.1

# 4. Disease_Prob 범위 재클립
df3["Disease_Prob"] = np.clip(df3["Disease_Prob"], 0, 1)

df3.to_csv("csv3.csv", index=False)