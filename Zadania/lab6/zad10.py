import datetime
import time

rok = int(input("Podaj rok: "))
miesiac = int(input("Podaj miesiąc: "))
dzien = int(input("Podaj dzień: "))

data = datetime.date(rok, miesiac, dzien)
dzien_roku = data.timetuple().tm_yday
tydzien = data.isocalendar()[1]

data_2_tygodnie_przed = data - datetime.timedelta(weeks=2)
data_2_tygodnie_po = data + datetime.timedelta(weeks=2)

dni_do_niedzieli = (6 - data.weekday()) % 7
najblizsza_niedziela = data + datetime.timedelta(days=dni_do_niedzieli)


czas_teraz = datetime.datetime(rok, miesiac, dzien, datetime.datetime.now().hour)
czas_unixowy = time.mktime(czas_teraz.timetuple())

print(data)
print(dzien_roku)
print(tydzien)
print(data_2_tygodnie_przed)
print(data_2_tygodnie_po)
print(dni_do_niedzieli)
print(najblizsza_niedziela)
print(czas_teraz)
print(czas_unixowy)
