import random
import time

def displayIntro(): 
    print("""Du bist in einem Lande voller Drachen. Es sind ZWEI Höhlen vor dir.
In einer Höhle ist der Drache friedlich, und wird sein Schatz mit dir teilen.
Und der andere Drache ist verdammt schlecht drauf, wie du es ja ahnen kannst,
und er wird dich 1. Fressen und 2. dein Blut trinken wie ein fucking Martini.
Und passt auf, bei dem Drachen-Martini alla "James Bond" werden die Oliven durch deine Augen ersetzt!""")   
    print()

def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("In welche Höhle willste rein gehn? (1 oder 2)")
        cave = input()
    return cave

def checkCave(chosenCave):
    print("Du nährst dich der Höhle...")
    time.sleep(2)
    print("Es ist dunkel und grußelig...")
    time.sleep(2)
    print("Ein großer Drache springt dich von vorne an! Er öffnet seine große FRESSE und und und ...") 
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print("gibt dir sein Schatz!")
    else:
        print("Mit einem mal verschlingt er dich...") 

playAgain = "ja"
while playAgain == "ja" or playAgain == "j":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Wilst du es nochmal spielen? (ja oder nein)")
    playAgain = input()