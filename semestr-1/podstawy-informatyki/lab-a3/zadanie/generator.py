import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def generate(amp, freq, gamma, t, noise_amp):
    result = amp * np.sin(2 * np.pi * freq * t) * np.exp(-gamma * t) + 2*noise_amp*(np.random.rand(len(t))-0.5)
    return result


while True:
    try:
        while True:
            time_max = float(input("Podaj zakres czasu:"))
            if time_max >= 0:
                break
            else:
                print("Nieprawidłowa wartość, spróbuj ponownie")
        break
    except ValueError:
        print("Nieprawidłowa wartość, spróbuj ponownie")
while True:
    try:
        while True:
            time_steps = int(input("Podaj liczbę kroków wektora czasu:"))
            if time_steps >= 0:
                time = np.linspace(0, time_max, time_steps)
                break
            else:
                print("Nieprawidłowa wartość, spróbuj ponownie")
        break
    except ValueError:
        print("Nieprawidłowa wartość, spróbuj ponownie")
while True:
    try:
        while True:
            amp = float(input("Podaj amplitudę sinusoidy:"))
            if amp >= 0:
                break
            else:
                print("Nieprawidłowa wartość, spróbuj ponownie")
        break
    except ValueError:
        print("Nieprawidłowa wartość, spróbuj ponownie")
while True:
    try:
        while True:
            freq = float(input("Podaj częstotliwość sinusoidy:"))
            if freq >= 0:
                break
            else:
                print("Nieprawidłowa wartość, spróbuj ponownie")
        break
    except ValueError:
        print("Nieprawidłowa wartość, spróbuj ponownie")
while True:
    try:
        while True:
            gamma = float(input("Podaj współczynnik wygaszenia:"))
            if gamma >= 0:
                break
            else:
                print("Nieprawidłowa wartość, spróbuj ponownie")
        break
    except ValueError:
        print("Nieprawidłowa wartość, spróbuj ponownie")
while True:
    try:
        while True:
            noise_amp = float(input("Podaj amplitudę szumu:"))
            if noise_amp >= 0:
                break
            else:
                print("Nieprawidłowa wartość, spróbuj ponownie")
        break
    except ValueError:
        print("Nieprawidłowa wartość, spróbuj ponownie")


values = generate(amp, freq, gamma, time, noise_amp)

choice = input("Czy chcesz zapisać wynik do pliku csv? [Y/n]:")
if not choice or (choice[0] != 'n' and choice[0] != "N"):
    filename = input("Podaj nazwę pliku:").strip()
    data = {"t": time, "a": values}
    dataframe = pd.DataFrame(data)
    dataframe.to_csv(filename, index=False, sep="\t")

plt.plot(time, values)
plt.show()

