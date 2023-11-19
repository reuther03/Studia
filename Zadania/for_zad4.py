n = int(input("Podaj liczbę naturalną n: "))
a = float(input("Podaj pierwszy wyraz ciągu:  "))
r = float(input("Podaj różnicę ciągu arytmetycznego: "))

for i in range(n):
    print(a + i * r)
