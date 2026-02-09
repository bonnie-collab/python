#A for loop can also be used to iterate a list , string or even a dictionary//

name= "okeyo"

for  letter in name:
    print(letter)

name = "okeyo"
for letter in name:
   if letter == "e":
     print("the letter e")
   else:
      print(letter)

print('===============')
#counties lists
counties = ["nairobi", "kisumu", "nakuru", "meru", "embu", "meru", "siaya", "mombasa", "kajiado", "kakamega",]

print(counties)

for county in counties:
   print(county)

print('===============')


 # for loop can also used to iterate through a dictionary

player = {
   "name": "mbape",
   "age": 25,
   "nationality": "french",
   "teams": ["psg", "monaco", "france"]
}

for key in player:
   print(key)

for values in player:
   print(player[values])

print('===============')
#loop through the teams he has played for
fruits = ["psg", "monaco", "france"]

for teams in player["teams"]:
    print(teams)

  
