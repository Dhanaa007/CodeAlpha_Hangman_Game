import random

# Dictionary of words and their hints
words = {
    "python": "A popular programming language",
    "computer": "An electronic device",
    "college": "A place for higher education",
    "keyboard": "Used for typing",
    "internet": "A worldwide network",
    "library": "A place where books are kept",
    "science": "Study of the natural world",
    "football": "A popular outdoor sport",
    "diamond": "A precious gemstone",
    "developer": "A person who writes software"
}

# Select a random word
word = random.choice(list(words.keys()))
hint = words[word]

guessed_letters = []
wrong_attempts = 0
max_attempts = 6

print("=" * 45)
print("          🎮 HANGMAN GAME")
print("=" * 45)

name = input("Enter your name: ").strip()

print(f"\nWelcome, {name}! ")
print("Guess the hidden word one letter at a time.")
print(f"You have {max_attempts} attempts.")
print("Type 'hint' anytime if you need a clue.\n")

while wrong_attempts < max_attempts:

    # Display current word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Attempts Left:", max_attempts - wrong_attempts)
    print("Guessed Letters:", " ".join(guessed_letters) if guessed_letters else "None")

    # Check if player won
    if "_" not in display:
        print(f"\n Congratulations, {name}!")
        print(f"You guessed the word: {word.upper()}")
        break

    guess = input("\nEnter a letter: ").lower().strip()

    # Hint
    if guess == "hint":
        print(" Hint:", hint)
        continue

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct or wrong
    if guess in word:
        print(" Correct Guess!")
    else:
        wrong_attempts += 1
        print(" Wrong Guess!")

# Game over
if wrong_attempts == max_attempts:
    print("\n Game Over!")
    print("The correct word was:", word.upper())

print("\nThank you for playing! ")