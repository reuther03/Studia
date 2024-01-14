def wypisz_imie_i_wiek(imie, wiek=20):
    """
    Wypisuje na ekranie imię i wiek.
    Jeśli wiek nie jest podany to wiek = 20.
    """
    print(f"Imię: {imie}, Wiek: {wiek}")

print(wypisz_imie_i_wiek.__doc__)

wypisz_imie_i_wiek("Michal")
wypisz_imie_i_wiek("Adam", 30)