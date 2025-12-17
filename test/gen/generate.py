import pandas as pd
import numpy as np

np.random.seed(42)

n = 100

# 나이, 성별, BMI, 혈압, 혈당, 콜레스테롤, 흡연, 운동
Age = np.random.randint(20, 70, n)
Gender = np.random.choice(['M', 'F'], n)
BMI = np.round(np.random.normal(25, 4, n), 1)
BloodPressure = np.round(np.random.normal(130, 10, n), 1)
Glucose = np.round(np.random.normal(100, 20, n), 1)
Cholesterol = np.round(np.random.normal(200, 30, n), 1)
Smoking = np.random.choice(['Yes', 'No'], n, p=[0.4, 0.6])
Exercise_per_week = np.random.randint(0, 8, n)

# Smoking 값 숫자로 변환
Smoking_num = np.where(Smoking=='Yes', 1, 0)

# Disease_Prob 계산 (선형 조합 + 노이즈)
Disease_Prob = (
    0.02*Age + 
    0.03*BMI + 
    0.015*BloodPressure + 
    0.02*Glucose + 
    0.01*Cholesterol + 
    0.1*Smoking_num - 
    0.05*Exercise_per_week +
    np.random.normal(0, 0.02, n)  # 작은 노이즈
)
# 0~1 범위로 제한
Disease_Prob = np.clip(Disease_Prob/10, 0, 1)
Disease_Prob = np.round(Disease_Prob, 2)

df = pd.DataFrame({
    'Age': Age,
    'Gender': Gender,
    'BMI': BMI,
    'BloodPressure': BloodPressure,
    'Glucose': Glucose,
    'Cholesterol': Cholesterol,
    'Smoking': Smoking,
    'Exercise_per_week': Exercise_per_week,
    'Disease_Prob': Disease_Prob
})

df.to_csv('synthetic_disease_data.csv', index=False)
print(df)