#python module
#is a file that contains python defination, statements and or function 

def add():
    num1=20
    num2=30
    sum= num1 + num2
    print("the answer", sum)

def subratact():
    x = 45
    y =30
    difference= x-y
    print("the difference is:", difference)

#these function above can be called by another file

def rectanglearea():
    length = int(input("enter the length of the rectangle: "))
    width = int(input("enter the width of the rectangle: "))

    area = length * width
    print("the area of the rectangle is:", area)


