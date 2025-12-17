import pandas as pd
import matplotlib.pyplot as plt

# CSV 3 불러오기
df3 = pd.read_csv("csv4.csv")

# NaN 제거
df3 = df3.dropna(subset=['BMI','Disease_Prob'])

# 산점도
plt.figure(figsize=(8,6))
plt.scatter(df3['BMI'], df3['Disease_Prob'])
plt.xlabel('BMI')
plt.ylabel('Disease_Prob')
plt.title('CSV 3: BMI vs Disease_Prob')
plt.grid(True)
plt.show()
