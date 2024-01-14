def oblicz_bmi(waga, wzrost):
    bmi = waga / (wzrost ** 2)

    if bmi < 18.5:
        print(f"Bmi: {bmi} niedowaga")
    elif 18.5 <= bmi < 25:
        print(f"Bmi: {bmi} Prawidlowa waga")
    elif 25 <= bmi < 30:
        print(f"Bmi: {bmi} nadwaga")
    else:
        print(f"Bmi: {bmi} otyłość")


print(oblicz_bmi(80, 1.80))