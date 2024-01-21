import random

random_numer = random.randrange(1,15)
rok_urodzenia = [2000, 2001, 2003, 2004, 2005]

print("szczesliwy numerek to:", random_numer)
print("szczesliwy rocznik to:", random.choice(rok_urodzenia))

trafione_liczby = 0
liczby_gracza = []
lista_liczb = random.sample(list(range(1, 50)), 6)
for x in range(1,7):
    liczba = int(input("podaj liczbe: "))
    liczby_gracza.append(liczba)

    if liczba in lista_liczb:
        trafione_liczby += 1

print("twoje liczby to:", liczby_gracza)
print("trafione liczby:", trafione_liczby)
print(lista_liczb)






