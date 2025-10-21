import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("health_dataset.csv")
plt.plot(data['Age'],color='r')

plt.show()




