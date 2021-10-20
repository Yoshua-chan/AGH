import math as math


def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def right_triangle_perimeter(a, b):
    return a + b + hypotenuse(a, b)


def right_triangle_area(a, b):
    return (a * b) / 2


a = float(input("a:"))
b = float(input("b:"))

print("Przeciwprostokatna:", hypotenuse(a, b))
print("Obwód:", right_triangle_perimeter(a, b))
print("Powierzchnia:", right_triangle_area(a, b))