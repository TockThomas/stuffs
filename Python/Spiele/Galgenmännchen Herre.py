import random

HANGMAN_PICS = ["""
    +---+
        |
        |
        |
       ===""", """
    +---+
    O   |
        |
        |
       ===""", """
    +---+
    O   |
    |   |
        |
       ===""", """
    +---+
    O   |
   /|   |
        |
       ===""", """
    +---+
    O   |
   /|\  |
        |
       ===""", """
    +---+
    O   |
   /|\  |
   /    |
       ===""", """
    +---+
    O   |
   /|\  |
   / \  |
       ===""", """
    +---+
   [O   |
   /|\  |
   / \  |
       ===""", """
    +---+
   [O]  |
   /|\  |
   / \  |
       ==="""]

words = {"Verteidiger": "smoke mute castle pulse doc rook tachanka kapkan jaeger bandit".split(),
         "Angreifer": "sledge thatcher ash thermit twitch montagne glaz fuze blitz iq".split()}

def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return wordDict[wordKey][wordIndex], wordKey

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("Fehlende Buchstaben:", end=" ")
    for letter in missedLetters:
        print(letter, end=" ")
    print()

    blanks = "_" * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=" ")
    print()

def getGuess(alreadyGuessed):
    while True:
        print("Tippen Sie eine Buchstabe.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("\nNur eine Buchstabe.")
        elif guess in alreadyGuessed:
            print("\nDu hast schon bereits diesen Buchstabe. Schreib nochmal.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("\nSchreib eine Buchstabe.")
        else:
            return guess

def playAgain():
    print("\nWillst du es nochmal spielen? (ja oder nein)")
    return input().lower().startswith("j")

print("H A N G M A N")

difficultygrade = "e m h".upper().split()
difficulty = ""
while difficulty not in difficultygrade:
    print("Gibt ein Schwierigkeitsgrad: E - Einfach, M - Mittel, H - Hart")
    difficulty = input().upper()
if difficulty == "M":
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
elif difficulty == "H":
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ""
correctLetters = ""
secretWord, secretSet = getRandomWord(words)

gameIsDone = False

while True:
    print("\nDein Wort ist von: " + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("\nDein Wort ist von: " + secretSet)
            displayBoard(missedLetters, correctLetters, secretWord)
            print("Richtig! Dein Wort war \"" + secretWord + "\"! Du hast gewonnen!")
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            print("\nDein Wort ist von: : " + secretSet)
            displayBoard(missedLetters, correctLetters, secretWord)
            print("Du hast keine Versuche mehr!\nNach " + str(len(missedLetters)) + " Fehlversuche und " + str(len(correctLetters)) + " richtige Versuche war der Wort \"" + secretWord + "\"")
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ""
            correctLetters = ""
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break 