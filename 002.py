import pandas as pd
import matplotlib.pyplot as plt

# CSV 2 불러오기
df2 = pd.read_csv("csv_3.csv")

# NaN 제거
df2 = df2.dropna(subset=['Cholesterol','Disease_Prob'])

# 산점도
plt.figure(figsize=(8,6))
plt.scatter(df2['Cholesterol'], df2['Disease_Prob'])
plt.xlabel('Cholesterol')
plt.ylabel('Disease_Prob')
plt.title('CSV 2: Cholesterol vs Disease_Prob')
plt.grid(True)
plt.show()
