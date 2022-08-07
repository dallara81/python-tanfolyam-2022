'''
Logikai operátorok
and     és
or      vagy
not     nem
'''

print('*** Negativitás-vizsgáló szuperapplikáció ***\n')

szam_c = int(input('Mondj egy egész számot!\n>>>'))
szam_d = int(input('Mondj még egy egész számot!\n(lehet negatív is te surmó!)\n>>>'))
if szam_c < 0 or szam_d < 0:
    print('Legalább az egyik szám negatív.')
if szam_c < 0 and szam_d < 0:
    print('Sőt, mi több! Mind a két szám negatív.')
if szam_c >= 0 and szam_d >= 0:
    print('Mindkét szám pozitív.')

