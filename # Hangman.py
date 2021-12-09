# Hangman
import random
print("Welcome to Hangman")
words = ['car', 'rainbow', 'tree', 'snow', 'nose', 'conference', 'explosion', 'eyes', 'by', 'computer', 'science', 'programming',
'python', 'mathematics', 'player', 'condition',
'reverse', 'water', 'board', 'garden', 'football', 'gaming', 'tennis', 'fire', 'ice', 'birthday', 'captain', 'tolerate']
word = random.choice(words)

guesses = []
turns = 6

while turns > 0:
    failed = 0

    for l in word:
        if (l in guesses): print(l, end="")
        else:
            print("_", end="")
            failed += 1
    print("\r")
    
    if (failed == 0):
        print("You Won!")
        print("The word was", word)
        break
    guess = input("Guess a Letter >> ").lower()

    guesses.append(guess)

    if (guess not in word):
        turns -= 1
        print("Wrong, you have", turns, "more guesses.")
        if (not turns > 0):
            print("You lost! The word was", word)