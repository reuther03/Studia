def silnie(n):
    if n == 0:
        return 1
    else:
        return n * silnie(n - 1)


n = int(input("Podaj liczbę naturalną n: "))

print(f"Silnia liczby {n} wynosi: {silnie(n)}")
