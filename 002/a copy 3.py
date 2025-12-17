import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("health_dataset_2.csv")

plt.scatter(df["Glucose"], df["Disease_Prob"], c=df["Age"], cmap="viridis", alpha=0.7)
plt.xlabel("Glucose")
plt.ylabel("Disease Probability")
plt.colorbar(label="Age")
plt.title("Glucose vs Disease Probability (Color=Age)")
plt.show()
