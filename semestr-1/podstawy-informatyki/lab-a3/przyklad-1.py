import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv(r'dane_pomiarowe.csv', sep="\t")
t = np.array(df['t'])
a = np.array(df['a'])

plt.plot(t, a)
plt.show()