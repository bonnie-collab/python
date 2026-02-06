#python list
#a list in python is a collection of items that are ordered in a certain way.
# a list is introduced by the use of the square brackets []
#the items of alist are stored insidenof indexes in programming we start counting from index zero
#a list is mutable the content of a list can be changed 

cars = ["BMW", "Benze", "Prado", "Probox", "Mclaren", "Range"]
print(cars)
print(type(cars))

#accessing items in a list
print(cars[2])
print("the car on the index is:", cars[4])


#list slicing - this is creatin a list from a given bigger list
print(cars[4:])

#printing from index 0 to 3
print(cars[:3])

#printing from the hiance to probox
print(cars[2:5])

#list mutability
#we use the functio append to add an ietm at the end of a list

cars.append("mercedes")
print(cars)

cars.append("subra")
print(cars)

#we use the pop function toremove an item at the end of the list
cars.pop()
print(cars)


#we can use an index to add items to alist
cars[5] = "pajero"
print = (cars)

#we can use the sort function to sort items in alphabetic order
cars.sort()
print()