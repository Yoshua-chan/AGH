import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def sine(t, gamma, amp, freq):
    result = amp * np.sin(2 * np.pi * freq * t) * np.e**(-gamma * t)
    return result


while True:
    try:
        filename = input("Podaj nazwę pliku do wczytania: ").strip()
        df = pd.read_csv(filename, sep="\t")
        t = np.array(df["t"])
        a = np.array(df["a"])
        break;
    except OSError:
        print("Nie ma takiego pliku, spróbuj ponownie")


plt.xlabel("t")
plt.ylabel("a")
plt.grid()

plt.scatter(t,a, s=2)

choice = input("Czy chcesz dokonać dopasowania? [Y/n]:")
if not choice or (choice[0] != 'n' and choice[0] != "N"):
    p0 = [0.15, 400, 0.1]
    fit_params, covariance_matrix = curve_fit(sine, t, a, p0=p0)

    print("Parametry dopasowania:\n")
    print("gamma =", fit_params[0])
    print("    A =", fit_params[1])
    print("    f =", fit_params[2])

    plt.title("$ a(t) = " + str(round(fit_params[1], 2)) + "\cdot \sin(2 \pi \cdot " + str(round(fit_params[2], 4)) + "\cdot t) \cdot e^{(-" + str(round(fit_params[0], 6)) + " \cdot t)}" + "$")
    plt.plot(t, sine(t, *fit_params), 'r')
else:
    plt.title("$a(x)$")

plt.show()