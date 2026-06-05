import random

WORDS = [
    "python",
    "hangman",
    "computer",
    "programming",
    "developer",
    "keyboard",
    "software",
    "internet",
    "puzzle",
    "challenge",
]

MAX_TRIES = 10


def choose_word():
    return random.choice(WORDS)


def display_state(word, guessed_letters, tries_left):
    display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print("\nWord:", display)
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print("Tries left:", tries_left)


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = set()
    tries_left = MAX_TRIES

    print("Welcome to Hangman!")
    print(f"You have {MAX_TRIES} wrong guesses. Good luck!")

    while tries_left > 0:
        display_state(word, guessed_letters, tries_left)

        guess = input("Enter a letter: ").strip().lower()
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed that letter.")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            wrong_guesses.add(guess)
            tries_left -= 1
            print("Wrong guess.")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")


if __name__ == "__main__":
    play_hangman()
