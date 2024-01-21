import random

x = int(input("Podaj dolna granice: "))
y = int(input("Podaj gorna granice: "))
num1 = 0
num2 = 0

if y < x:
    num1 = y
    num2 = x
else:
    num1 = x
    num2 = y

tupla_liczb = tuple(random.randint(num1, num2) for z in range(10))

print(tupla_liczb)
print(sum(tupla_liczb)/ 10)
