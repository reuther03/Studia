a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
if b > a:
    num1 = a
    num2 = b
elif a > b:
    num1 = b
    num2 = a

while num1 <= num2:
    print(num1 * num2)
    num1 += 1