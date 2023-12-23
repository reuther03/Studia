name = input("Podaj imię: ")
print(f"Witaj {name}")

age = int(input("Podaj wiek: "))
print(f"Twój wiek to: {age}")

imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")
print(f"{imie[0]}{nazwisko[0]}")

str = input("Podaj łańcuch znaków: ")
print(str * 5)

string1 = input("Podaj pierwszy łańcuch: ")
string2 = input("Podaj drugi łańcuch: ")

str1 = string1 + string2
str2 = string1[:len(string1)//2] + string2[len(string2)//2:]
print(str1)
print(str2)