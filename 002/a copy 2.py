import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("health_dataset_2.csv")
plt.scatter(df["BMI"], df["Disease_Prob"], alpha=0.5)
plt.xlabel("BMI")
plt.ylabel("Disease Probability")
plt.title("Complex Data: BMI vs Disease_Prob (raw)")

# 고혈당자만
df_high_glu = df[df["Glucose"] >= 140]
plt.scatter(df_high_glu["BMI"], df_high_glu["Disease_Prob"], c='red')
plt.xlabel("BMI (Glucose >= 140)")
plt.ylabel("Disease Probability")
plt.title("BMI vs Disease_Prob for High Glucose")
plt.show()