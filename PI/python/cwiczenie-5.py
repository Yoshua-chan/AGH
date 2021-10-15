import matplotlib.pyplot as plt
import math as m
tab=[]
z=0

amp = float(input("Podaj amplitude:"))
x_axis = int(input('Podaj zakres:'))

for x in range(1, x_axis):
    val = amp * m.sin(z)
    if val == 0:
        print("val = 0, dla val =", val)
    tab.append(val)
    z = z + 0.1
plt.plot(tab)
plt.axis([0, x_axis, -1.5 * amp, 1.5 * amp])
plt.show() # wyświetlenie wykresu