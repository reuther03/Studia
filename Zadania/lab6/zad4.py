import datetime


czas_aktualny = datetime.datetime.now()
zajecia = datetime.datetime(2024, 1, 15)
kolokwium = datetime.datetime(2024, 2, 12)

print(czas_aktualny)
print("ostatnie zajecia byly:", czas_aktualny - zajecia)
print("kolokwium bedzie za: ", kolokwium - czas_aktualny)

