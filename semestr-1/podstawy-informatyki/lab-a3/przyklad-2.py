import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

t = np.linspace(-10, 10, 100)
y = t*t
data = {"t": t, "y": y}
dataframe = pd.DataFrame(data)
dataframe.to_csv("new.csv", index=False, sep="\t")

df = pd.read_csv(r"new.csv", sep="\t")
t = np.array(df["t"])
y = np.array(df["y"])
plt.plot(t, y)
plt.show()
