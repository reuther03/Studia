x = int(input("Podaj wysokość choinki: "))

for i in range(1, x + 1):
    print("* " * i)


y = int(input("Podaj wysokość choinki: "))

for i in range(1, y + 1):
    print(" " * (y - i) + "* " * i)