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
guessed_letters = set()
print(" _ " * len_word)
count1 = 10
while count1 > 0:
    current_guess = input(f"Guess the {len_word} lettered word!\n").lower()
    count1 -= 1
    print(f"You have {count1} chances more!")

    while (
        len(current_guess) != 1
        or current_guess in list(string.punctuation)
        or current_guess in list(string.digits)
    ):

        current_guess = input(f"Please input single Alphabet only.\n").lower()

    while current_guess in guessed_letters:
        current_guess = input(
            f"You already tried with '{current_guess}' guess again!\n"
        )

    if current_guess in random_word.lower() and current_guess not in guessed_letters:
        guessed_letters.add(current_guess)

        for letter in random_word.lower():
            if letter in guessed_letters:
                print(f" {letter} ", end=(""))

                continue
            else:
                print(" _ ", end=(""))

                continue
if count1 == 0:
    print("Failed")
