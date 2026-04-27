"""
Task 1: Hangman Game
Internship: CodeAlpha -- Python Programming
Author: Anselm Munango
Description: A console-based Hangman game where the player guesses letters to reveal a hidden word.
             The game provides feedback on correct and incorrect guesses, tracks the number of attempts,
                and vissually represents progress through a staged-based hangman system.
                This project demonstrates the use of functions, loops, conditionals, sets, and basic I/O in Python.
"""

import random


# -- Configuration constants for the hangman game ----------------------------------
# These values define the rules and behavior of the game.
WORD_LIST = ["developer", "detour", "function", "internship", "python"]
MAX_INCORRECT_GUESSES = 6

HANGMAN_STAGES = [
    "stage 0",
    "stage 1",
    "stage 2",
    "stage 3",
    "stage 4",
    "stage 5",
    "stage 6",
]


# --User Interface------------------------------------------------------------
# Functions responsible for displaying game information and getting user input are defined here.
def display_state(stage_index, word, guessed_letters, incorrect_letters):
    """Render the current game state, including the hangman stage, the word with guessed letters revealed, and the list of incorrect guesses."""
    print(HANGMAN_STAGES[stage_index])
    print("\nWord: ", end="")
    print(" ".join(letter if letter in guessed_letters else "_" for letter in word))
    print(
        "\nIncorrect guesses ({}/{}): {}".format(
            len(incorrect_letters),
            MAX_INCORRECT_GUESSES,
            ", ".join(sorted(incorrect_letters)) if incorrect_letters else "None"
        )
    )
    print("-" * 40)


# -- Input validation ----------------------------------------------------------
def get_player_guess(guessed_letters):
    while True:
        guess = input("Enter a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
        elif guess in guessed_letters:
            print("You already guessed '{}'. Try a different letter.".format(guess))
        else:
            return guess


# -- Game loop -----------------------------------------------------------------
def play_hangman():
    word = random.choice(WORD_LIST)
    guessed_letters = set()
    incorrect_letters = set()

    print("\n" + "=" * 40)
    print("       Welcome to Hangman!")
    print("=" * 40)
    print("A {}-letter word has been chosen. Good luck!\n".format(len(word)))

    while True:
        display_state(len(incorrect_letters), word, guessed_letters, incorrect_letters)

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word: '{}'".format(word.upper()))
            break

        if len(incorrect_letters) >= MAX_INCORRECT_GUESSES:
            print("\nGame over. The word was: '{}'".format(word.upper()))
            break

        guess = get_player_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print("'{}' is in the word!".format(guess))
        else:
            incorrect_letters.add(guess)
            remaining = MAX_INCORRECT_GUESSES - len(incorrect_letters)
            print("'{}' is not in the word. {} chance(s) remaining.".format(guess, remaining))


# -- Entry point ---------------------------------------------------------------
def main():
    while True:
        play_hangman()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThanks for playing. Goodbye.")
            break


if __name__ == "__main__":
    main()
