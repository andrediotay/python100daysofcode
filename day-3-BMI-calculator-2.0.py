# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight/height**2

if bmi < 18.5:
    interpretation = "are underweight"
elif bmi < 25:
    interpretation = "have a normal weight"
elif bmi < 30:
    interpretation = "are slightly overweight"
elif bmi < 35:
    interpretation = "are obese"
else:
    interpretation = "are clinically obese"

print(f"Your BMI is {round(bmi)}, you {interpretation}.")

#test comment for git