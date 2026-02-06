# A tuple == is an imutable type of a lsit and it cannot change 
# to introduce a tuple we introduce a parathnesis
counties =("nairobi", "mombasa", "Nakuru", "kisii", "kajiado", "Eldoret")
print(counties)
print(type(counties))

#slicing of tupples
print(counties[3:])

#accessing items of a tuple by use of the indexes
print(counties[3])

#accesing items of a tupple by the use of the indexes
print(counties[4])

#accessing items below will gwnwrate an error
counties.append("machakos")
print(counties)