'''
Ciklusok - Input-tal
(egyszerű gyakorlópélda)
'''

folytat = True
while folytat:
    print('Húzd meg a ravaszt!')
    valasz = input('Nehezedre esik? (i/n) ')
    if valasz == 'n':
        folytat = False
print('Na végre...')