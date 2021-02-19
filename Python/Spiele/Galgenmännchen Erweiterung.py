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

words = {"name": "mert daniel adrian nowak soenmez schleicher thomas inac can kiril".split(),
         "defense": "smoke mute castle pulse doc rook tachanka kapkan jaeger bandit".split(),
         "attacker": "sledge thatcher ash thermit twitch montagne glaz fuze blitz iq".split()}

def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return wordDict[wordKey][wordIndex], wordKey

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print("Missed letters:", end=" ")
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
        print("Guess a letter.")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("\nPlease enter a single letter.")
        elif guess in alreadyGuessed:
            print("\nYou have already guessed that letter. Choose again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("\nPlease enter a LETTER.")
        else:
            return guess

def playAgain():
    print("\nDo you want to play again? (yes or no)")
    return input().lower().startswith("y")

print("H A N G M A N")

difficultygrade = "e m h".upper().split()
difficulty = ""
while difficulty not in difficultygrade:
    print("Enter difficulty: E - Easy, M - Medium, H - Hard")
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
    print("\nThe secret word is in the set: " + secretSet)
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
            print("\nThe secret word is in the set: " + secretSet)
            displayBoard(missedLetters, correctLetters, secretWord)
            print("Yes! The Secret word is \"" + secretWord + "\"! You have won!")
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            print("\nThe secret word is in the set: " + secretSet)
            displayBoard(missedLetters, correctLetters, secretWord)
            print("You have run out of guesses!\nAfter " + str(len(missedLetters)) + " missed guesses and " + str(len(correctLetters)) + " correct guesses, the word was \"" + secretWord + "\"")
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ""
            correctLetters = ""
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break 