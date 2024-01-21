import math
def pole_trojkata(a, b, kąt):

    if a <= 0 or b <= 0 or kąt <= 0 or kąt >= 90:
        return "Nieprawidłowe dane: boki muszą być dodatnie, a kąt ostry."

    kąt_rad = math.radians(kąt)

    pole = 0.5 * a * b * math.sin(kąt_rad)

    return pole

print(pole_trojkata(5,7,60))