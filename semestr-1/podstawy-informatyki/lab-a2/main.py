import numpy as np

def sphere_volume(radius): 
    return 4/3 * np.pi * (radius ** 3)

def sphere_area(radius):
    return 4 * np.pi * (radius ** 2)



def tetrahedron_volume(edge):
    return (edge ** 3)/(6 * np.sqrt(2))

def tetrahedron_area(edge):
    return np.sqrt(3) * (edge ** 2)



def pyramid_volume(edgeA, edgeB, height):
    return 1/3 * edgeA * edgeB * height;
    
def pyramid_area(edgeA, edgeB, height):
    Pp = edgeA * edgeB

    #Ściana przy edgeA
    height_A = np.sqrt((1/2 * edgeB) ** 2 + height ** 2)
    Pa = (edgeA * height_A)/2

    #Ściana przy edgeB
    height_B = np.sqrt((1/2 * edgeA) ** 2 + height ** 2)
    Pb = (edgeB * height_B)/2

    return Pp + 2 * Pa + 2 * Pb



def cone_volume(radius, height):
    Pp = np.pi * (radius ** 2)
    return 1/3 * Pp * height

def cone_area(radius, height):
    Pp = np.pi * (radius ** 2)
    l = np.sqrt((height ** 2) + (radius ** 2))



def cylinder_volume(radius, height):
    return np.pi * (radius ** 2) * height

def cylinder_area(radius, height):
    return 2 * np.pi * radius * (radius + height)


def elipsoid_area(a, b):
    if b > a:
        temp = a
        a = b
        b = temp
    epsilon = np.sqrt(1 - (b ** 2 / a ** 2))
    P = 2 * np.pi * b * (b + a/epsilon * np.arcsin(epsilon))
    return P

def display_stuff(name, area, volume, density):
    print("\n" + name + ":")
    if area != 0:
        print("Pole powierchni:", area, "[m^2]")
    if volume != 0:
        print("Objętość:", volume, "[m^2]")
    if density != 0:
        print("Gęstość:", density, "[kg/m^3]")
    if density != 0 and volume != 0:
        print("Masa: ", (density * volume), "[kg]")
    print()





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
                    area = elipsoid_area(a, b)
                    display_stuff("Elipsoida obrotowa", area, 0, 0)
                    repeat = 0


        else:
            print("Niepoprawna opcja, spróbuj ponownie")
            continue
            repeat = 1

        yes = input('Czy chcesz skorzystać z programu jeszcze raz? [Y/n]: ')
        if yes != "n" and yes != "N":
            print()