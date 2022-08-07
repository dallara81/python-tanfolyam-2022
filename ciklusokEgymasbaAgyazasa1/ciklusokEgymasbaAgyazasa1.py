'''
Ciklusok egymásba ágyazása 1.
(egyszerű példa)
'''


sor = 1
while sor <= 7:
    oszlop = 1
    while oszlop <= 7:
        print('O ', end='') # Alapértelmezésben end='\n', de megváltoztatható bármire ezen a módon
        oszlop = oszlop + 1
    print('') # soremelés csak
    sor = sor + 1