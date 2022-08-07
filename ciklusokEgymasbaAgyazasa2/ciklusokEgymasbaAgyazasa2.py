'''
Ciklusok egymásba ágyazása 2.
(egyszerű példa)
'''


darab = 1
sor = 1
while sor <= 7:
    oszlop = 1
    while oszlop <= darab:      # A "darab" valtozóval definiáltam az "O"-k számát
        print('O ', end='')     # Alapértelmezésben end='\n', de megváltoztatható bármire ezen a módon
        oszlop = oszlop + 1
    print('') # soremelés csak
    darab = darab + 1           # Az "O"-k száma minden a sor minden lefutásakot +1 elemmel bővül
    sor = sor + 1