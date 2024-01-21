import random

print("Gra w zgadywanie liczby")

x = int(input("Podaj dolną granicę zakresu: "))
y = int(input("Podaj górną granicę zakresu: "))

if y < x:
    dolna, gorna = y, x
else:
    dolna, gorna = x, y

liczba = random.randint(dolna, gorna)

for proba in range(3):
    zgadnij = int(input("Zgadnij liczbę: "))

    if zgadnij == liczba:
        print("Zgadłeś!")
        break
    elif zgadnij < liczba:
        print("Za mało!")
    else:
        print("Za dużo!")

else:
    print(f"Niestety, nie udało się. Liczba to: {liczba}")