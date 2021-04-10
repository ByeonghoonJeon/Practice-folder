# Greeting.
# Make a list of word candidate.
# Pick a random word.
# Show as many underbar as letters in the random word.
# Ask "Guess letter"
# Check if input is valid. (No numbers, no more than single letter)
# If input is valid,
# Check if input is in the letter.
# If input is matching to a letter in the random word,
# Remove underbar and show letter(s).
# If input is NOT matching to a letter in the random word,
# Print "You lost one chance and there is n-1 chances left."
# And go to line 5.
# If input is invalid,
# Print "Please input only single letter."
# And go to line 5 again.
import random
import string

print("Welcome to Jeon's Hangman program.")
word_list = [
    "Assignment",
    "Agreement",
    "Argument",
    "Astronaut",
    "Abbreviation",
    "Agriculture",
    "Abusement",
    "Aardvark",
    "Bureaucracy",
    "Beautiful",
    "Bilingual",
    "Beethoven",
    "Circumstance",
    "Chromatography",
    "Chondroitin",
    "Cucumber",
    "Creativity",
    "Chewable",
    "Cooperation",
    "Communication",
    "Colonization",
    "Clarithromycin",
    "Dysphagia",
    "Dimentia",
    "Duplication",
    "Dimension",
    "Denmark",
    "Derivative",
    "Dungeon",
    "Desparado",
    "Ethiopia",
    "Elongation",
    "Erythromycin",
    "Estrogen",
    "Elastinase",
    "Esquire",
    "Electrophoresis",
    "Euphoria",
    "Finalization",
    "Fabulous",
    "Frequency",
    "Feminism",
]


random_word = random.choice(word_list)
len_word = int(len(random_word))
guessed_letters = []
print(" _ " * len_word)

current_guess = input(f"Guess the {len_word} lettered word!\n").lower()

while True:
    while (
        len(current_guess) != 1
        or current_guess in list(string.punctuation)
        or current_guess in list(string.digits)
    ):
        current_guess = input(f"Please input single Alphabet only.\n").lower()
    guessed_letters += current_guess
    for guessed_letters in random_word.lower():
        if guessed_letters in random_word.lower():
            print(f"{guessed_letters}")
            continue
        elif guessed_letters not in random_word.lower():
            current_guess = input("Please try again!")
            continue
        elif random_word.lower() in guessed_letters:
            print("Splendid!")
            break
print("The end.")


# random_word = random.choice(word_list)
# len_word = int(len(random_word))
# guessed_letters = set()
# print(" _ " * len_word)
# while True:
#     guess_letter = input(f"Guess the {len_word} lettered word!\n").lower()

#     while (
#         len(guess_letter) != 1
#         or guess_letter in list(string.punctuation)
#         or guess_letter in list(string.digits)
#     ):

#         guess_letter = input(f"Please input single Alphabet only.\n").lower()

#     if guess_letter in random_word.lower() and guess_letter not in guessed_letters:
#         guessed_letters.add(guess_letter)

#     for letter in random_word.lower():
#         if letter in guessed_letters:
#             print(f" {letter} ", end=(""))
#             continue
#         else:
#             print(" _ ", end=(""))
#             continue
