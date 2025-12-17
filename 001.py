import pandas as pd
import matplotlib.pyplot as plt

# CSV 1 불러오기
df1 = pd.read_csv("csv_3.csv")

# NaN 제거
df1 = df1.dropna(subset=['Glucose','Disease_Prob'])

# 산점도
plt.figure(figsize=(8,6))
plt.scatter(df1['Glucose'], df1['Disease_Prob'])
plt.xlabel('Glucose')
plt.ylabel('Disease_Prob')
plt.title('CSV 1: Glucose vs Disease_Prob')
plt.grid(True)
plt.show()
