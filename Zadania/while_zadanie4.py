a = int(input("Podaj liczbę: "))
b = int(input("Podaj liczbę: "))

if a > b:
    num1 = b
    num2 = a
else:
    num1 = a
    num2 = b

while num1 <= num2:
    if num1 % 2 == 0:
        print(num1)
    num1 += 1
