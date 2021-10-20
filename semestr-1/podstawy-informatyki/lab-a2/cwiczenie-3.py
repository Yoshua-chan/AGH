import math as math


def hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)


def is_right_triangle(a, b, c):
    return 1 if c == hypotenuse(a, b) else 0


print("3, 4, 5:", is_right_triangle(3, 4, 5))
print("3, 4, 6:", is_right_triangle(3, 4, 6))