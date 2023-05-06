import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

life = 7
guess = input("Guess a letter: ").lower()
if guess in chosen_word:
    for letter in chosen_word:
        if letter == guess:
            print("Right")
        else:
            print("Wrong")
else:
    life -= 1
    print(life)