imie = input("Wprowadź swoje imię: ")
print("Witaj", imie)


wiek = input("Wprowadź swój wiek: ")
print("Twój wiek to:", wiek)


imie = input("Wprowadź swoje imię: ")
nazwisko = input("Wprowadź swoje nazwisko: ")
inicjaly = imie[0] + nazwisko[0]
print("Twoje inicjały to:", inicjaly)

lancuch = input("Wprowadź łańcuch znaków: ")
print(lancuch * 5)

lancuch1 = input("Wprowadź pierwszy łańcuch: ")
lancuch2 = input("Wprowadź drugi łańcuch: ")
polaczony_lancuch = lancuch1 + lancuch2
print("Połączony łańcuch:", polaczony_lancuch)

lancuch1 = input("Wprowadź pierwszy łańcuch: ")
lancuch2 = input("Wprowadź drugi łańcuch: ")
polowa_pierwszego = lancuch1[:len(lancuch1)//2]
polowa_drugiego = lancuch2[len(lancuch2)//2:]
nowy_lancuch = polowa_pierwszego + polowa_drugiego
print("Nowy łańcuch:", nowy_lancuch)