n = int(input("Podaj liczbę studentów: "))
students = n
suma = 0
while n > 0:
    punkty = int(input(f"Podaj ilosc punktów dla studenta nr.{n}: "))
    if punkty > 100 or punkty < 0:
        print("Nie można uzyskać więcej niż 100 punktów.")
        continue
    print(f"Student {n} uzyskał {punkty} punktów.")
    n -= 1
    suma += punkty
    if n == 0:
        print(f"Średnia punktów wynosi.", suma / students)