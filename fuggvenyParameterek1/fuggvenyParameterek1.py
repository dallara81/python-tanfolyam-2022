def print_tomato_soup_recipe(cheese_type, side_dish):
    print('Pirítsd meg olívaolajon a hagymát és fokhagymát.')
    print('Tedd hozzá a felkockázott paradicsomot, sózd és borsozd meg, majd öntsd fel 2 dl vízzel.')
    print('Főzd kis lángon 15-20 percig.')
    print('Ha szétfőtt a paradicsom, add hozzá a száraz kenyeret, olívaolajat, bazsalikomot, és adj hozzá egy kis vizet.')
    print('Főzd még 5 percig.')
    print('Szórj rá reszelt ' + cheese_type + '-t.')
    print('Szolgáld fel ' + side_dish + '-val/vel.')

print_tomato_soup_recipe('edami', 'pogácsa') # függvény meghívása a paraméterek megadásával kell történjen!

'''
1. Egy függvénynek természetesen több paramétere is lehet. Ezeket vesszővel választjuk el, lésd 1. sor!
Az argumentum a konkrét érték, amelyet megadunk a függvény paraméterének a függvényhívás (function call) során.
'''