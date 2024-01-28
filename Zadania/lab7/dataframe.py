import pandas as pd

data = {
    'nr_albumu': ["w11111", "w22222", "w33333", "w44444", "w55555"],
    'imie': ['Anna', 'Bartek', 'Cezary', 'Dorota', 'Ewa'],
    'nazwisko': ['Nowak', 'Kowalski', 'Wiśniewski', 'Zając', 'Mazur'],
    'oceny': [4.5, 3.0, 5.0, 4.0, 4.5],
    'wiek': [20, 22, 21, 23, 19]
}
df = pd.DataFrame(data)

student = df[df['oceny'] > 4]
print(student)

sorted = df.sort_values(by='wiek')
print(sorted)

grupa = df.groupby('oceny')['wiek'].mean()
print(grupa)

poprawa = {
    'nr_albumu': ["w11111", "w33333", "w55555"],
    'oceny_poprawka': [5.0, 4.5, 5.0]
}

df_poprawa = pd.DataFrame(poprawa)
df2 = pd.merge(df, df_poprawa, on='nr_albumu', how='left')
print(df2)

plik = 'C:\Repos\Studia\Zadania\lab7\zad.csv'
df2.to_csv(plik, index=False)
df3 = pd.read_csv(plik)

nowy_student = {'nr_albumu': "w66666", 'imie': 'Filip', 'nazwisko': 'Jankowski', 'oceny': 4.0, 'wiek': 20}
df4 = df.append(nowy_student, ignore_index=True)
print(df3)

oceny = df['oceny'].unique()
print(oceny)

studenci5 = df[df['oceny'] == 5].shape[0]
print(studenci5)
