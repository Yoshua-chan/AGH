from scipy.fft import fft 
from generator import *
import pandas as pd
from scipy.io.wavfile import write
import scipy.signal as signal
import matplotlib.pyplot as plt

def TranformataFouriera(t,y): 
    N = len(t) 
    dt = t[1] - t[0] 
    yf = 2.0 / N * np.abs(fft(y)[0:N // 2]) 
    xf = np.fft.fftfreq(N, d=dt)[0:N // 2] 
    return xf, yf

while True:
    while True: # Sampling rate
        try:
            sampling = int(input("Podaj częstotliwość próbkowania [Hz]:"))

            if sampling <= 0:
                raise ValueError

            break
        except ValueError:
            print("Niepoprawna wartość, spróbuj ponownie")

    while True: # Timespan
        try:
            timespan = float(input("Podaj czas trwania sygnału [s]:"))

            if timespan <= 0:
                raise ValueError

            break
        except ValueError:
            print("Niepoprawna wartość, spróbuj ponownie")

    while True: # X limit
        try:
            x_limit = float(input("Podaj zakres rysowania wykresu [s]:"))

            if x_limit <= 0:
                raise ValueError

            break
        except ValueError:
            print("Niepoprawna wartość, spróbuj ponownie")



    while True:
        try:
            print("[1] Sine")
            print("[2] Square")
            print("[3] Sawtooth")
            print("[4] Triangle")
            print("[5] White noise")
            wav_num = input("Wybierz przebieg jaki chcesz wygenerować:")

            if(wav_num != "1" and wav_num != "2" and wav_num != "3" and wav_num != "4" and wav_num != "5"):
                raise ValueError
            
            break
        except ValueError:
            print("Niepoprawna wartość, spróbuj ponownie")

    while True: # Frequency
        try:
            frequency = float(input("Podaj częstotliwość sygnału [Hz]:"))

            if frequency <= 0:
                raise ValueError

            break
        except ValueError:
            print("Niepoprawna wartość, spróbuj ponownie")

    while True: # Amplitude
        try:
            amplitude = float(input("Podaj amplitudę sygnału:"))

            if amplitude <= 0:
                raise ValueError

            break
        except ValueError:
            print("Niepoprawna wartość, spróbuj ponownie")


    generator = Function_generator(sampling, timespan)

    if wav_num == "1":
        waveform_data = generator.sine(amplitude, frequency)
    elif wav_num == "2":
        waveform_data = generator.square(amplitude, frequency)
    elif wav_num == "3":
        waveform_data = generator.sawtooth(amplitude, frequency)
    elif wav_num == "4":
        waveform_data = generator.triangle(amplitude, frequency)
    elif wav_num == "5":
        waveform_data = generator.WhiteNoise(amplitude)

    
    choice = input("Czy chcesz zapisać przegieg do pliku wav? [Y/n]:")
    if choice != "n" and choice != "N":
        filename = input("Podaj nazwę pliku wav:").strip()
        audio_data = np.int16(waveform_data * 2**14)
        write(filename, sampling, audio_data)
    
    choice = input("Czy chcesz zapisać przegieg do pliku csv? [Y/n]:")
    if choice != "n" and choice != "N":
        filename = input("Podaj nazwę pliku csv:").strip()
        csv_data = {"t": generator.time, "v": waveform_data}
        dataframe = pd.DataFrame(csv_data)
        dataframe.to_csv(filename, index=False, sep="\t")

    plt.plot(generator.time, waveform_data)
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.xlim(0, x_limit)
    plt.show()



    choice = input("Czy chcesz skorzystać z programu jeszcze raz? [Y/n]:")
    if choice == "n" or choice == "N":
        exit(0)