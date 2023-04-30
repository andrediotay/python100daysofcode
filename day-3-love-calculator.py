# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


t_ = (name1 + name2).lower().count("t")
r_ = (name1 + name2).lower().count("r")
u_ = (name1 + name2).lower().count("u")
e_ = (name1 + name2).lower().count("e")
l_ = (name1 + name2).lower().count("l")
o_ = (name1 + name2).lower().count("o")
v_ = (name1 + name2).lower().count("v")
e_ = (name1 + name2).lower().count("e")

score = (t_ + r_ + u_ + e_)*10 + l_ + o_ + v_ + e_

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
