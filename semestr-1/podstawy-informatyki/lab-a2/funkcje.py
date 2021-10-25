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
