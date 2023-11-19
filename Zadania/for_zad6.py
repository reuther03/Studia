while True:
    dana = int(input("Wprowadź liczbę: "))
    if dana > 0:
        print("To jest liczba")
        print(f"Pierwiastek kwadratowy liczby {dana} to {dana**0.5}")
        continue
    else:
        print("Dziękujemy za skorzystanie z naszej aplikacji.")
        break