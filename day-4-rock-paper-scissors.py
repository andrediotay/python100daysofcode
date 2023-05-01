import random

p_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
c_choice = random.randint(0,2)

rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """
paper = """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """
scissors = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
win_map = [["draw","lose","win"],["win","draw","lose"],["lost","win","draw"]]
image_list = [rock,paper,scissors]

print(image_list[p_choice])

print(f"Computer chose:")
print(image_list[c_choice])

print(f"You {win_map[p_choice][c_choice]}.")
#improved