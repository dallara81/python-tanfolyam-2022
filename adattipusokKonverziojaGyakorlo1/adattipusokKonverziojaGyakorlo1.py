'''Típusátalakítás - avagy típuskonverzió
Itt a szám, ott a szöveg!'''

#szöveg >>> szám
szam = 44
print(szam)
print("Mi a típusod, gyík!?")
print(type(szam))
print('\n')

print('Nézzük, miféle-fajta állat vagy: \nszam = str(szam)')
szam = str(szam)
print (szam)
print("Nos, gyík... ezek után mi a típusod?")
print(type(szam))

print('\nNe szövegelj (itten stringgel)! Tudsz tizedest is?\nszam = 44 + 0.44')
szam = 44 + 0.44
print (szam)
print("Lássuk, nem-e csak az arcod volt nagy!")
print(type(szam))

print("\nRendben gyík, a mai napot túlélted - de ne bízd el magad!")