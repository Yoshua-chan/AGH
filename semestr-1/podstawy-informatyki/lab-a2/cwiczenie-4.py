import numpy as np


def get_triangle_angles(a, b, c):
    angles = []
    angles.append(np.degrees(np.arccos((a**2 + b**2 - c**2) / (2*a*b))))
    angles.append(np.degrees(np.arccos((a ** 2 + c ** 2 - b ** 2) / (2*a*c))))
    angles.append(np.degrees(np.arccos((b ** 2 + c ** 2 - a ** 2) / (2*b*c))))
    return angles


print(get_triangle_angles(100, 100/2, 100*(np.sqrt(3)/2)))