import random

words = ("dict", "python", "java", "hangman", "github")
word = random.choice(words)
turns = 8
guesses = ''
use_latter = []


def menu():
    while True:
        choice = input("HANGMAN" "\nThe game will be available soon." "\n1. Play" "\n2. Exit" "\n")
        if choice == '1' or choice == 'Play':
            print("Wellcome!\n")
            game(turns, guesses)
        if choice == '2' or choice == 'Exit':
            print("Goodbye!")
            return


def game(turns, guesses):
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                print(end="")
                failed += 1
        if failed == 0:
            print("You win!")
            print("Guessed word: ", word)
            break
        print()
        guess = input("Input:>")
        guesses += guess
        if guess.upper():
            print("Input only small letters!")
        if len(guess) > 1:
            print("Too much letters, input only 1 letter!")
        elif guess in use_latter:
            print("This letter has already guessed!")
        else:
            use_latter.append(guess)
        if guess not in word:
            turns -= 1
            print("Incorrect")
            print("You have only", + turns, 'guesses!')
            if turns == 0:
                print("You lose!" "\nWhat a pity!")

menu()




