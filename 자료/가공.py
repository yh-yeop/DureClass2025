import pandas as pd
import numpy as np

df = pd.read_csv("csv_3.csv")

# 숫자 컬럼으로 변환
for col in ['BMI', 'BloodPressure', 'Glucose', 'Cholesterol']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 현실적 범위 벗어난 값 제거
df = df[df['Glucose'].between(50, 250)]
df = df[df['Cholesterol'].between(100, 300)]
df = df[df['BMI'].between(10, 50)]
df = df[df['BloodPressure'].between(80, 180)]
df = df[df['Age'].between(1, 150)]
df = df[df['Disease_Prob'].between(0, 1)]

# 문자 이상값 제거
df.loc[~df['Gender'].isin(['M','F']), 'Gender'] = np.nan
df.loc[~df['Smoking'].isin(['Yes','No']), 'Smoking'] = np.nan
df['Disease_Prob']=df['Disease_Prob'].round(2)

# 대체 코드
# smoking = df['Smoking'].tolist()
# smoking = [s if s in ['Yes','No'] else None for s in smoking]
# df['Smoking'] = smoking

# smoking = df['Smoking'].tolist()

# smoking = [s if s in ['Yes','No'] else None for s in smoking]
# smoking_list=[]
# for i in smoking:
#     if i in ['Yes','No']:
#         smoking_list.append(i)
#     else:
#         smoking_list.append(np.nan)
# df['Smoking'] = smoking



df.to_csv("csv_3_cleaned.csv", index=False)