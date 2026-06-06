import random

words = [
    ("python", "a popular programming language"),
    ("guitar", "a musical instrument"),
    ("apple", "a fruit"),
    ("ocean", "a large body of salt water"),
    ("mountain", "a tall landform"),
]

word, hint = random.choice(words)
max_wrong = 6
wrong_guesses = set()
guessed_letters = set()

print("Welcome to Hangman!")
print(f"Hint: {hint}")

while True:
    display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print("\nWord:", display)
    print("Wrong guesses:", " ".join(sorted(wrong_guesses)))
    print(f"Remaining attempts: {max_wrong - len(wrong_guesses)}")

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word.")
        break

    if len(wrong_guesses) >= max_wrong:
        print(f"Game over. The word was: {word}")
        break

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
        print("Wrong guess.")
