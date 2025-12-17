import pandas as pd
import numpy as np

np.random.seed(42)
n = 100

# 공통 기본 데이터 생성
def generate_base_data(n):
    Age = np.random.randint(20, 70, n)
    Gender = np.random.choice(['M', 'F'], n)
    BMI = np.round(np.random.normal(25, 4, n), 1)
    BloodPressure = np.round(np.random.normal(130, 10, n), 1)
    Glucose = np.round(np.random.normal(100, 20, n), 1)
    Cholesterol = np.round(np.random.normal(200, 30, n), 1)
    Smoking = np.random.choice(['Yes', 'No'], n, p=[0.4, 0.6])
    Exercise_per_week = np.random.randint(0, 8, n)
    return Age, Gender, BMI, BloodPressure, Glucose, Cholesterol, Smoking, Exercise_per_week

# 1번 CSV (정상 데이터, 관계 뚜렷)
Age, Gender, BMI, BloodPressure, Glucose, Cholesterol, Smoking, Exercise_per_week = generate_base_data(n)
Smoking_num = np.where(Smoking=='Yes', 1, 0)
Disease_Prob = (
    0.02*Age + 0.03*BMI + 0.015*BloodPressure + 0.02*Glucose + 0.01*Cholesterol + 0.1*Smoking_num - 0.05*Exercise_per_week +
    np.random.normal(0, 0.02, n)
)
Disease_Prob = np.clip(Disease_Prob/10, 0, 1)
Disease_Prob = np.round(Disease_Prob, 2)
df1 = pd.DataFrame({
    'Age': Age, 'Gender': Gender, 'BMI': BMI, 'BloodPressure': BloodPressure,
    'Glucose': Glucose, 'Cholesterol': Cholesterol, 'Smoking': Smoking,
    'Exercise_per_week': Exercise_per_week, 'Disease_Prob': Disease_Prob
})
# df1.to_csv('csv_1.csv', index=False)

# 2번 CSV (이레귤러 일부 추가)
df2 = df1.copy()
# 상위 10% 행에 대해 랜덤하게 Disease_Prob 재설정 → 다른 변수와 관계 약화
irregular_idx = np.random.choice(df2.index, size=10, replace=False)
df2.loc[irregular_idx, 'Disease_Prob'] = np.round(np.random.rand(10), 2)
# df2.to_csv('csv_2.csv', index=False)

# 3번 CSV (결측치 추가)
df3 = df2.copy()
# 무작위로 결측치 추가
for col in ['Age', 'BMI', 'BloodPressure', 'Glucose', 'Cholesterol', 'Exercise_per_week']:
    idx = np.random.choice(df3.index, size=5, replace=False)
    df3.loc[idx, col] = np.nan
# Smoking, Gender에도 일부 결측 추가
df3.loc[np.random.choice(df3.index, 3, replace=False), 'Smoking'] *=10
df3.loc[np.random.choice(df3.index, 3, replace=False), 'Gender'] *=10

df3.to_csv('csv_3.csv', index=False)