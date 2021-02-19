import random
import time

guessesTaken = 0

print("Hallo! Wie heißt du?")
myName = input()

print("Also " + myName + ".")
time.sleep(1)

print("Du wirst gleich einen Zahl erraten und du darfst die Spielregeln selbst entscheiden.")
time.sleep(1)

print("Cool oder? :D\n")
time.sleep(2)

print("Du wirst jetzt eine Zahlreihefolge eingeben.")
time.sleep(1)
print("Erste Zahl ist sollte der Anfang der Zahlreihefolge bestimmen")
time.sleep(1)
print("und der zweite Zahl das Ende der Zahlreihefolge.")

zahlanfang = input()
zahlende = input()

print("Jetzt gibst du ein, wie viele Versuche du haben willst.")

versuche = input()

number = random.randint(int(zahlanfang), int(zahlende))
print("Also, " + myName + ", ich überlege mir ein Zahl zwischen " + zahlanfang + " bis " + zahlende + " und du hast nur " + versuche + " Versuche.\n")

for guessesTaken in range(int(versuche)):
    print("Schätze eine Zahl.")
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Dein Schätzung ist zu niedrig.")

    if guess > number:
        print("Dein Schätzung ist zu hoch.")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print("\nGut gemacht, " + myName + "! Du hast erfolgreich meine Zahl in " + guessesTaken + " von " + versuche + " Versuche erraten!")

if guess != number:
    number = str(number)
    print("Nein. Die Zahl war " + number + ".")