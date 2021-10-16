# Proszę samodzielnie stworzyć program pozwalający na obliczanie miejsc
# zerowych funkcji kwadratowej. W zależności od ilości miejsc zerowych
# wyświetlana powinna być ich ilość. Następnie proszę wyświetlić wykres tej funkcji
# i porównać otrzymane miejsca zerowe.

import math as math
import matplotlib.pyplot as plt
import numpy as np

#TODO place roots of quadratic formula on the plot

def geteq(a, b, c):

    if a != 0:
        equation = str(a) + "x^2"

    if b < 0:
        equation = equation + str(b) + "x"
    elif b > 0:
        equation = equation + "+" + str(b) + "x"

    if c < 0:
        equation = equation + str(c)
    elif c > 0:
        equation = equation + "+" + str(c)

    return equation

def getvalue(a, b, c, x):
    value = a*(x ** 2) + b*x + c
    return value

def getxrange(x1, x2):
    delta = abs(x2 - x1)
    x_range = 1.5 * delta
    return x_range

def getyrange(q):
    return abs(q)

a = int(input('Wprowadź a:'))
b = int(input('Wprowadź b:'))
c = int(input('Wprowadź c:'))

Δ = (b**2) - (4*a*c)
p = -b / (2 * a)
q = -Δ / (4 * a)



if Δ < 0:
    print("Funkcja " + geteq(a, b, c) + " nie ma miejsc zerowych")
    exit(0)
else:

    x1= (-b-math.sqrt(Δ)) / (2*a)
    x2= (-b+math.sqrt(Δ)) / (2*a)

    print("Miejsca zerowe funkcji " + geteq(a, b, c) + ":")
    print("x1 =", x1, "\nx2 =", x2)

    x_range = getxrange(x1, x2)
    
    args = np.arange(-x_range, x_range, 0.1)
    vals = getvalue(a, b, c, args)

    plt.axhline(y=0, color='black', linestyle='--') # rysuje y=0 przerywaną linią
    plt.plot(args, vals) # rysuje wykres wartości od argumentów
    plt.show()
