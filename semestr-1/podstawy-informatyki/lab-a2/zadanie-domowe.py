import numpy as np
from funkcje import *

#TODO: Napisać zestaw funkcji pozwalające na obliczenie: objętości, masy, pola powierzchni: 
#TODO: a) kuli (10%)* 
#TODO: b) czworościanu foremnego (10%)* 
#TODO: c) ostrosłupa prostego o podstawie prostokątnej (10%)* 
#TODO: d) stożka (10%)* 
#TODO: e) walca (10%)* 
#TODO: f) elipsoidy (20%)*,** * jeżeli funkcje obliczające objętości, masy, pola powierzchni działają poprawnie 

# Program powinien wyświetlając wszystkie wymienione nazwy brył które zostały zaimplementowane, 
# następnie poprosić użytkownika o dokonanie wyboru jednej z nich. Po dokonaniu wyboru program 
# powinien wyświetlić listę właściwości, które wylicza (objętość, masa, pole powierzchni). Pod 
# dokonaniu wyboru użytkownik podaje potrzebne parametry (o które zostanie poproszony) a następnie 
# wyświetla wynik wybranej operacji (objętości, masy, pola powierzchni) dla wybranej bryły

# W całym programie w wyświetlanych komunikatach należy stosować jednostki układu SI 

# Program powinien być zapętlony, tzn. po wyliczeniu zadanej wartości dla zadanej bryły powinien pytać 
# użytkownika czy chce kontynuować i wykonać inne obliczenia, podobnie jak w zadaniu 6.

# Program powinien posiadać zabezpieczenie przed podaniem wartości niedozwolonych (np. liczb 
# ujemnych lub łańcuchów znaków i innych koniecznych warunków jeśli występują) i informować o tym 
# fakcie użytkownika w poprzez wyświetlenie odpowiedniego komunikatu, jednocześnie kontynuując 
# działanie i prosząc o podanie poprawnej wartości


yes = 'Y';
while yes != 'n' and yes != "N":
    print("[1] Kula")
    print("[2] Czworościan foremny")
    print("[3] Ostrosłup prosty o podstawie prostokątnej")
    print("[4] stożek")
    print("[5] Walec")
    print("[6] elipsoida obrotowa")

    repeat = 1
    while repeat == 1:


        figure = input("Wybierz figurę której parametry chcesz obliczyć (wprowadź odpowiadającą jej cyfrę):")
        

# ========== KULA ========== #
        if figure == "1":
            dim_correct = 0 
            while dim_correct == 0:
                radius = float(input("Podaj promień kuli [m]:"))
                density = float(input("Podaj gęstość [kg/m^3]:"))
                if radius <= 0 or density <= 0:
                    print("Niepoprawne parametry: wszystkie parametry muszą być dodatnie")
                    dim_correct = 0
                else:
                    dim_correct = 1
                    volume = sphere_volume(radius)
                    area = sphere_area(radius)
                    display_stuff("Kula", area, volume, density)
                    repeat = 0


# =============== CZWOROŚCIAN ============ #
        elif figure == "2":
            dim_correct = 0 
            while dim_correct == 0:
                edge = float(input("Podaj długość krawędzi czworościanu [m]:"))
                density = float(input("Podaj gęstość [kg/m^3]:"))
                if edge <= 0 or density <= 0:
                    print("Niepoprawne parametry: wszystkie parametry muszą być dodatnie")
                    dim_correct = 0
                else:
                    dim_correct = 1
                    volume = tetrahedron_volume(edge)
                    area = tetrahedron_area(edge)
                    display_stuff("Czworościan foremny", area, volume, density)
                    repeat = 0



# =========== OSTROSŁUP ============ #
        elif figure == "3":
            dim_correct = 0 
            while dim_correct == 0:
                edgeA = float(input("Podaj bok A podstawy ostrosłupa [m]:"))
                edgeB = float(input("Podaj bok B podstawy ostrosłupa [m]:"))
                height = float(input("Podaj wysokość ostrosłupa [m]:"))
                density = float(input("Podaj gęstość [kg/m^3]:"))
                if edgeA <= 0 or height <= 0 or edgeB <= 0 or density <= 0:
                    print("Niepoprawne parametry: wszystkie parametry muszą być dodatnie")
                    dim_correct = 0
                else:
                    dim_correct = 1
                    volume = pyramid_volume(edgeA, edgeB, height)
                    area = pyramid_area(edgeA, edgeB, height)
                    display_stuff("Ostrosłup prosty prostokątny", area, volume, density)
                    repeat = 0


# =========== STOŻEK ============ #
        elif figure == "4": 
            dim_correct = 0
            while dim_correct == 0:
                radius = float(input("Podaj promień podstawy stożka [m]:"))
                height = float(input("Podaj wysokość stożka [m]:"))
                density = float(input("Podaj gęstość [kg/m^3]:"))
                if radius <= 0 or height <= 0 or density <= 0:
                    print("Niepoprawne parametry: wszystkie wymiary muszą być dodatnie")
                    dim_correct = 0 
                else:
                    dim_correct = 1
                    volume = cone_volume(radius, height)
                    area = cone_area(radius, height)
                    display_stuff("Stożek", area, volume, density)
                    repeat = 0



# =========== WALEC ============ #
        elif figure == "5": #walec
            dim_correct = 0 
            while dim_correct == 0:
                radius = float(input("Podaj promień podstawy walca [m]:"))
                height = float(input("Podaj wysokość walca [m]:"))
                density = float(input("Podaj gęstość [kg/m^3]:"))
                if radius <= 0 or height <= 0 or density <= 0:
                    print("Niepoprawne parametry: wszystkie parametry muszą być dodatnie")
                    dim_correct = 0 
                else:
                    dim_correct = 1
                    volume = cylinder_volume(radius, height)
                    area = cylinder_area(radius, height)
                    display_stuff("Walec", area, volume, density)
                    repeat = 0
                    

# ========= ELIPSOIDA ========== #
        elif figure == "6": 
            dim_correct = 0 
            while dim_correct == 0:
                a = float(input("Podaj półoś A elipsoidy [m]:"))
                b = float(input("Podaj półoś B elipsoidy [m]:"))
                if a <= 0 or b <= 0:
                    print("Niepoprawne parametry: wszystkie parametry muszą być dodatnie")
                    dim_correct = 0 
                else:
                    dim_correct = 1
                    elipsoid_area(a, b)
                    display_stuff("Elipsoida obrotowa", area, 0, 0)
                    repeat = 0


        else:
            print("Niepoprawna opcja, spróbuj ponownie")
            continue
            repeat = 1

        yes = input('Czy chcesz skorzystać z programu jeszcze raz? [Y/n]: ')
        if yes != "n" and yes != "N":
            print()