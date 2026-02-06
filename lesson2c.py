# A dictionary is a data type that store data in terms of key - value pair
# Adictionary is introduced by the use of curly braces {}
#the values stored inside a dictionary can be of any data type
# to access the values to a dictionary we use the keys

phonebook = {
    "Bonface" : "2546787795",
    "Amina" : "2547868699",
    "omondi" : "254888787",
}

#showing  the entire dictionary
print(phonebook)
print(type(phonebook))

#printing out the omondi number
print(phonebook["omondi"])

player = {
    "name": "messi",
    "age": "44",
    "teams": ["psg", "barcelona", "argentina"],
    "more":{
        "children": 3,
        "residence": "us",
        "phone" : (56565777, 7575775, 4434333)
    }
}
#print barcelona
print(player["teams"][1])