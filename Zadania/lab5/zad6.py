def pole_trojkata(a, b, c):
    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Błędne dane, boki nie mogą utworzyć trójkąta"

    s = (a + b + c) / 2

    pole = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return pole

print(pole_trojkata(3,4,6))