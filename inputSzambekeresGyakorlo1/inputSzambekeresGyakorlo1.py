'''Ez a fránya input... alapból mindig stringbe olvassa be a számaimat...
...de velem nem babrál ki!'''

kor = int(input('Hány éves vagy kicsi csíra?\n>>>'))

print('\nEllenőrzés: ')
print(kor)
print(type(kor))

print('\nAz eszed alapján a fele sem vagy!')
print(kor / 2-1)