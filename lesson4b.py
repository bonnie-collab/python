#Loops===sometimes we may need to do a piece of work a number of work repeated cenaarios in such case we may use looops 
#A loop is a controller structure that allows us to excute a block of code repeatedly until a certain conditoo is made 
# there 2 types of loops in python i.e the for loop and the while looop

#below is the syntax for loop

"""
for variable in range(n):
    #block of code to be excuted
"""

for greeting in range(20):
    print("hello moses", greeting)

print('===========================')
for number in range(10, 20):
    print(number)


print('===========================')
# find the even numbers from the range of 50 to 71

for number in range(50, 71, 2):
    print(number)


# find the odd numbers from the range of 100 to 150
for number in range(100, 151):
    if number % 2 != 0:
        print(number)

print('===========================')

#create a program that prints the multiples of 3 starting from 201 to 150
for number in range(201, 149, -1):
    if number % 3 == 0:
        print(number)

print('===========================')
#create a python program that prints the leap years in btween years 2000 and 2024
for year in range(2000, 2025, 4):
        print(year)