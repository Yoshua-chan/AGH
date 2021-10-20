def cuboid_volume(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return -1
    else:
        return a * b * c


def cuboid_area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return -1
    else:
        return (2 * a * b) + (2 * a * c) + (2 * b * c)


def get_mass(vol, density):
    return vol * density


def get_cuboid_mass(a, b, c, density):
    volume = cuboid_volume(a, b, c)
    return get_mass(volume, density)

a = float(input("Podaj długość boku a w metrach:"))
b = float(input("Podaj długość boku b w metrach:"))
c = float(input("Podaj długość boku c w metrach:"))
density = float(input("Podaj gęstość prostopadłościanu w kg/m^3:"))

print("Masa prostopadłościanu:", get_cuboid_mass(a, b, c, density), "kg")
