'''Van egy feltételes feltételem...
... ha feltétlen feltételem megleled!'''

szamfeltet = int(input('Villámgyorsan bevésel ide egy egész számot!\n>>>'))
if szamfeltet < 0:
    print('A megadott szám negatív.')
else:
    print('A megadott szám nem negatív.\n')
if szamfeltet > 0:
    print('A megadott szám pozitív.')
if szamfeltet == 0:
    print('A megadott szám nulla')
elif szamfeltet > 0:
    print('Már úgy elágaztam, hogy nem tudom hol vagyok... de próbálok pozitív maradni')

print('\n(c) 2022 Nagyonjó Nagyonfinom Szoftver Co.')