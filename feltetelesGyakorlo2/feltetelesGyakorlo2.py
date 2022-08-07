'''Nyuszi ül a fűben,
ne tudd meg mit művel!'''

import random

randomszam = random.randint(-2, 2)
print(randomszam)

if randomszam > 0:
    print('Pozitív,')
elif randomszam < 0:
    print('Negatív,')
else:
    print('Ez bizony nulla, erről nem érdemes vitatkozni...')

if randomszam % 2 == 0:
    print('és páros a szám.')
else:
    print('és páratlan a szám.')
if randomszam == 0:
    print('Ne vakarózz! Fogadjunk, hogy nem tudtad, hogy a nulla páros szám!')