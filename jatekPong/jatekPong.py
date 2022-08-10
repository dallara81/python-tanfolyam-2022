'''
PONG játék a Turtle plugin felhasználásával
'''


import turtle               # erre is van egy importálható modul, ami nem egy rossz dolog, hehe!

#JÁTÉKTÉR

jatekter = turtle.Screen()                  # játéktér definiálása
jatekter.setup(width=1024, height=768)      # játéktér mérete
jatekter.bgcolor("black")                   # gáttérszín
jatekter.title('PONG')                      # neve
jatekter.tracer(0)                          # kilépéshez!


# Ütő 1, jobb oldalon

utoJobb = turtle.Turtle()                    #
utoJobb.speed(0)                             # nem megy sehova - egyenlőre
utoJobb.shape("square")                     # forma
utoJobb.shapesize(stretch_wid=6, stretch_len=1)
utoJobb.color("white")
utoJobb.penup()
utoJobb.goto(470,0)


# Ütő 2, bal oldalon

utoBal = turtle.Turtle()                    #
utoBal.speed(0)                             # nem megy sehova - egyenlőre
utoBal.shape("square")                      # forma
utoBal.shapesize(stretch_wid=6, stretch_len=1)
utoBal.color("white")
utoBal.penup()
utoBal.goto(-480,0)

# LABDA

labda = turtle.Turtle()
labda.speed(0)
labda.shape("circle")
labda.color("white")
labda.penup()
labda.goto(0,0)
labda.valtozasX = 0.25                                # labda mozgatása x koordinátán
labda.valtozasY = -0.25                               # labda mozgatása y koordinátán

# PONTSZÁMÍTÁS

pontszamJobb = 0
pontszamBal = 0

pontszam = turtle.Turtle()
pontszam.speed(0)
pontszam.color("white")
pontszam.penup()
pontszam.hideturtle()
pontszam.goto(0, 300)
pontszam.write(f"JÁTÉKOS 1> {pontszamJobb}                 JÁTÉKOS 2> {pontszamBal}", align="center",
               font=("Curier", 32, "normal"))


def utoBal_fel():                           # DEfiniál egy "utoBal_fel" nevű függvényt
    y = utoBal.ycor()                       # y koordinátán mozog csak
    y += 64                                 # y + 64 is nyilván helyes, 64 pixellel mozgatjuk (gomnyomásra majd)
    utoBal.sety(y)

def utoBal_le():
    y = utoBal.ycor()
    y -= 64
    utoBal.sety(y)

def utoJobb_fel():                           # DEfiniál egy "utoBal_fel" nevű függvényt
    y = utoJobb.ycor()                       # y koordinátán mozog csak
    y += 64                                  # y + 64 is nyilván helyes, 64 pixellel mozgatjuk (gomnyomásra majd)
    utoJobb.sety(y)

def utoJobb_le():
    y = utoJobb.ycor()
    y -= 64
    utoJobb.sety(y)

# BILLENTYŰZETFIGYELÉS

jatekter.onkey(utoBal_fel, "w")             # "w" megnyomására
jatekter.onkey(utoBal_le, "s")              # "s" megnyomására

jatekter.onkey(utoJobb_fel, "o")             # "w" megnyomására
jatekter.onkey(utoJobb_le, "k")              # "k" megnyomására

jatekter.listen()                           # figyeljen!


while True:

    # képernyő folyamatos frissítése
    jatekter.update()

    labda.setx(labda.xcor() + labda.valtozasX)
    labda.sety(labda.ycor() + labda.valtozasY)

    # "fal" létrehozása felül, pattanjon vissza
    if labda.ycor() > 372:
        labda.sety(372)                         # ennél tovább ne menjen!
        labda.valtozasY *= -1                   # visszafordítja a labdát

    # "fal" létrehozása alul, pattanjon vissza
    if labda.ycor() < -372:
        labda.sety(-372)                        # ennél tovább ne menjen!
        labda.valtozasY *= -1                   # visszafordítja a labdát (mint y * -1)

    # jobb oldal érintése
    if labda.xcor() > 470:
        labda.goto(0,0)                         # mewnjen vissza a kezdőpontra (kiment a labda!
        labda.valtozasX *= -1                   #induljon el most a másik irányba!
        pontszamBal += 1
        pontszam.clear()                        # teljes pontszám sor törtlése
        pontszam.write(f"JÁTÉKOS 1> {pontszamJobb}                 JÁTÉKOS 2> {pontszamBal}", align="center",
                       font=("Curier", 32, "normal"))


    # bal oldal érintése
    if labda.xcor() < -480:
        labda.goto(0,0)
        labda.valtozasX *= -1
        pontszamJobb += 1
        pontszam.clear()
        pontszam.write(f"JÁTÉKOS 1> {pontszamJobb}                 JÁTÉKOS 2> {pontszamBal}", align="center",
                       font=("Curier", 32, "normal"))


    # bal ütőről való visszapattanás
    if utoJobb.xcor()-20 < labda.xcor() < utoJobb.xcor() and utoJobb.ycor()-50 < labda.ycor() < utoJobb.ycor()+50:
        labda.setx(utoJobb.xcor()-20)
        labda.valtozasX *= -1

    # jobb ütőről való visszapattanás
    if utoBal.xcor()+20 > labda.xcor() > utoBal.xcor() and utoBal.ycor()-50 < labda.ycor() < utoBal.ycor()+50:
        labda.setx(utoBal.xcor()+20)
        labda.valtozasX *= -1
