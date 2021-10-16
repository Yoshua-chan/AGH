# Zadanie domowe:
# W języku python proszę napisać program, który:

#1. Pobierze od użytkownika parametry a, b, c, d wielomianu 4-tego stopnia
# wyświetlając odpowiednie zapytania (1 pkt)

#2. Wyświetli równanie wielomianu z uwzględnieniem znaków pobranych
# parametrów, np. 1*x^2 + 2*x -5 zamiast 1*x^2 + 2*x + -5, może przydać
# się print('A', end = '',) (2 pkt)

#3. Pobierz od użytkownika zakres, dla jakiego ma zostać narysowana funkcja,
# wraz ze sprawdzeniem czy zakres ma sens (w przypadku błędu zakończ
# działanie programu funkcją quit()) (2pkt)

#4. Narysuj wykres funkcji w podanym przez użytkownika zakresie za pomocą
# linii ciągłej. wykres powinien mieć około 100 punktów (4 pkt)

#5. Opisz osie wykresu jako ‘x’ oraz ‘f(x)’ (1 pkt)


import math as math
import matplotlib.pyplot as plt
import numpy as np

def geteq(a, b, c, d):
    params=[d, c, b, a]
    sign=""
    equation=""
    i = 3 
    while i > 0:
        if params[i] > 0:
            equation = equation + sign + str(params[i]) + "x^" + str(i + 1) 
            sign="+"
        elif params[i] < 0:
            equation = equation + str(params[i]) + "x^" + str(i + 1) 
            sign="+"
        i -= 1

    if params[i] > 0:
        equation = equation + sign + str(params[i]) + "x"
        sign="+"
    elif params[i] < 0:
        equation = equation + str(params[i]) + "x" 
        sign="+"

    return equation

def getvalue(a, b, c, d, x):
    value = a*(x**4) + b*(x**3) + c*(x**2) + d*x
    return value

a = float(input('Wprowadź a:'))
b = float(input('Wprowadź b:'))
c = float(input('Wprowadź c:'))
d = float(input('Wprowadź d:'))
x_range_low  = float(input('Podaj dolny zakres:'))
x_range_high = float(input('Podaj górny zakres:'))

if x_range_low >= x_range_high:
    print("błąd: górny zakres mniejszy lub równy od dolnego")
    exit(1)
    

args = np.arange(x_range_low, x_range_high, 0.1)
vals = getvalue(a, b, c, d, args)

print("\nWzór funkcji:")
print(geteq(a, b, c, d))

plt.xlabel("x")
plt.ylabel("f(x)")

plt.title("$f(x) = " + geteq(a, b, c, d) + "$")  # przekaż tytuł jako LaTeX

plt.axhline(y=0, color='black', linestyle='--') # rysuje y=0 przerywaną linią
plt.plot(args, vals) # rysuje wykres wartości od argumentów
plt.show()
