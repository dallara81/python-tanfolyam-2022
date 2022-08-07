'''
Ciklusok - Adatbekérő
(egyszerű gyakorlópélda)
'''


szam = int(input('Kérek egy egész számot 1 és 10 között!\n >>> '))

# while szam < 1 or 10 < szam:      # megoldás-1
while not 1 <= szam <= 10:          # megoldás-2
    szam = int(input('Látom, nem vetted le a lényegét! 0 és 10 közti egész szám, kapisch?\n >>> '))

print('Csak sikerült...')