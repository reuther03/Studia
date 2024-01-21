from time import sleep

sekundy = int(input("Podaj ilosc sekund"))

while sekundy > 0:
    print("pozostaly czas w sekundach to: ", sekundy)
    sekundy -= 1
    sleep(1)