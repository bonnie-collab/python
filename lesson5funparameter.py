#function with a parameter
#are value that get passed as arguments given to a function inside of the paranthesis

def greeting(name):
    print(f"{name} how are you")

greeting("okeyo")

print("---------------")

def message(names):
    print(f"{names} we shall be having a message on date 44 olease avail yourself")

message("musyoka")
message("stevo")
message("kariuki")

#for x in range(200)

#create function that accepts parameters to add 2 numbers

def add(x,y):
    sum = x + y
    print( "print sum of number is", sum)

add(34, 66)

# Test 1

# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)

# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.

def interest(p, r, t):
    i = p * r * t/100
    print("the simple interest is", i)

interest(4500, 7, 4/100)

