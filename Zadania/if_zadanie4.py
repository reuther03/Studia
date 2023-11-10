a = int(input("podaj pierwsza liczbe: "))
b = int(input("podaj druga liczbe: "))
c = int(input("podaj trzecia liczbe: "))

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)
