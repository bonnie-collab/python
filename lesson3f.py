#create a python program that is able to determine wether a number entered is an old number or an even number
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is Even")

elif number % 2 != 0:
    print("The number is Odd")

else:
    print("Invalid input")

#create a python program wether a person can donate blood according to age and weight. if weight is greater than 50kg and age is above 18 he can be able to donate the blood

age = int(input("Enter your age: "))
weight = float(input("Enter your weight (kg): "))

if age >= 18 and weight > 50:
    print("You are eligible to donate blood")

elif age < 18 and weight > 50:
    print("You are not eligible: Age must be 18 or above")

elif age >= 18 and weight <= 50:
    print("You are not eligible: Weight must be above 50 kg")

else:
    print("You are not eligible: Age must be 18+ and weight above 50 kg")

