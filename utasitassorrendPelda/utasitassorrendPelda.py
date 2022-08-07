some_variable = 123
some_expression = 2 + 2

def some_function():
    print('1. utasítás')
    print('2. utasítás')
    print('3. utasítás')

some_function()
print('Ez egy string.')
some_function()

'''
Utasítássorrend példa
(2.7. Milyen sorrendben hajtódik végre a Python-kód)

A control flow (magyarul vezérlésáram) az a sorrend, amelyben a Python interpreter beolvassa az utasításaidat.
A legegyszerűbb esetben a control flow felülről lefelé halad, és sorról sorra hajtja végig a Python statementeket.

Ez egészen addig igaz, amíg az interpreter nem fut bele valamibe, ami megváltoztatja a control flow-t, például egy függvénybe.


A FENTI PÉLDA
Amikor lefuttatod a fenti programot, a control flow (az utasítások végrehajtásának sorrendje) a következőképp alakul:

    Az interpreter elindul legfelülről, és létrehozza a some_variable változót az 1. sorban.
    Az interpreter lép egyet lefelé, létrehozza a some_expression változót, kiértékeli a 2 + 2 összeadást, 
    és elrakja az eredményét, azaz a 4-et a változóba.
    A 4. sorban az interpreter észleli a some_function() függvény deklarációt, de egyelőre nem csinál semmit, 
    mert nem hívtuk meg a függvényt. Eddig a control flow az alapbeállítást követi: megy felülről lefelé.
    A control flow első változása a 9. sorban következik, ahol meghívjuk a some_function() függvényt. 
    Az interpreter visszateleportál a 4. sorba, ahol a függvénydeklaráció található. 
    Végiglépdel a függvénytörzsön, és kiírja a három stringet. Amikor a 7. sorban eléri a függvény végét, 
    visszateleportál a 9. sorba, és folytatja az útját az alapértelmezett control flow szerint.
    A 10. sorban talál egy egyszerű print() függvényt, amit végrehajt.
    A 11. sorban újabb függvényhívás (function call) szerepel, úgyhogy az interpreter ismét teleportál. 
    A 4. sorban megtalálja a some_function() függvényt, végigmegy a törzsön, végrehajtja, 
    a függvény végén pedig visszateleportál a kiindulási helyére, azaz a 11. sorba.
    Az interpreter észleli, hogy véget ért a program, és leáll.

Ahogy látod, a függvények speciálisak abból a szempontból, hogy megtörik az alapértelmezett control flow-t.
'''