import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
scatter=plt.scatter(df["BloodPressure"], df["Cholesterol"], c=df["Smoking"], s=df["Exercise_per_week"]*10)
plt.colorbar(scatter, label="Smoking")
plt.xlabel("Blood Pressure")
plt.ylabel("Cholesterol")
plt.show()
