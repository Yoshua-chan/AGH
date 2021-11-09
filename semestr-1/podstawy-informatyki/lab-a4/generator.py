import numpy as np
import scipy.signal as signal
import random as random
from scipy.fft import fft


class Function_generator:

    def __init__(self, sampling_rate, timespan):
        self.sampling_rate = sampling_rate
        self.timespan = timespan
        self.time = np.linspace(0, timespan, timespan * sampling_rate)

    def sine(self, amplitude, frequency):
        return amplitude * np.sin(2 * np.pi * frequency * self.time)


    def square(self, amplitude, frequency):
        return amplitude * (np.sign(np.sin(2 * np.pi * frequency * self.time)))


    def sawtooth(self, amplitude, frequency):
        return signal.sawtooth(2 * np.pi * frequency * self.time) * amplitude

    
    def triangle(self, amplitude, frequency):
        return signal.sawtooth(2 * np.pi * frequency * self.time, 0.5) * amplitude
        return signal.t
    
    def WhiteNoise(self, amplitude):
        return (np.random.rand(len(self.time)) - 0.5) * 2 * amplitude

