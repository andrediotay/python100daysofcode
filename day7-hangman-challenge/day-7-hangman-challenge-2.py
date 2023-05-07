import random
from hangman_art import stages,logo
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)

life = 6
display = []
is_complete = 0
for letter in chosen_word:
    display.append("_")

while life != 0 and is_complete != len(chosen_word):
    guess = input("Guess a letter: ").lower()

    count = 0

    if guess in chosen_word:
        for letter in chosen_word:
            if letter == guess:
                display[count] = guess
            count += 1
    else:
        life -= 1

    is_complete = 0
    for char in display:
        if char != "_":
            is_complete += 1

    print(" ".join(display))
    print(stages[life])
if is_complete == len(chosen_word):
    print("You Win!")
elif life == 0:
    print("You Lose!")