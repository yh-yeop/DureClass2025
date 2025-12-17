import pandas as pd
import numpy as np

# 샘플 데이터
data = {
    'Age': [25, 30, 150, 45],
    'BMI': [22.5, 18.2, 100.0, 27.3],
    'Gender': ['M', 'F', 'X', 'F'],
    'Smoking': ['Yes', 'No', 'Maybe', 'Yes']
}

df = pd.DataFrame(data)

# Gender가 M 또는 F인지 확인
mask = df['Gender'].isin(['M', 'F'])
print("Gender가 M 또는 F인가?:\n", mask)

# 조건에 맞지 않는 값 NaN으로 변경
df.loc[~df['Gender'].isin(['M', 'F']), 'Gender'] = np.nan
df.loc[~df['Smoking'].isin(['Yes', 'No']), 'Smoking'] = np.nan

print()
print(df)

