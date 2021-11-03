
# *** Modulous ***
x = 15
if x % 5 == 0:
    print(x)

# *** Dictionary ***
person_two = {
    "name" : "Rob", #String
    "age" : 45, #Number
    "fav_colour" : "Purple", #String
    "food_truck" : True, #Boolean
    "items" : ["apple pie", "pumpkin", "peach", ["ice cream", "whip cream", "m&m's",]], #List
            #     0             1         2
    "address" : {"Chicago", "Illinois"} } #Dictionary

print(person_two['items'][1])
print(person_two['items'][3][0])

person_two['fav_colour'] = "Green"
person_two['food_truck'] = False

print(person_two)

person_three = {}
person_three['name'] = "Ramsey"
print(person_three)

person_two = {
    "name" : "Rob", #String
    "age" : 45, #Number
    "fav_colour" : "Purple", #String
    "food_truck" : True, #Boolean
    "items" : ["apple pie", "pumpkin", "peach", ["ice cream", "whip cream", "m&m's",]], #List
            #     0             1         2
    "address" : ["Chicago", "Illinois"]
}

val_removed = person_two.pop("age")
print(val_removed)

del person_two["fav_colour"]
print(person_two)

# Key of Keys
print(person_two.keys())

# Value of Values
print(person_two.values())

# Keys and Values
print(person_two.items())

# *** Conditionals ***

x = 53
if x > 50:
    print("Bigger than 50")
    print("Bigger than 50")
elif x > 30:
    print('Larger than 30')
elif x > 20:
    print('Larger than 20')
else:
    print('Is less than 10')

# Pass
x = 42
if x > 32:
    pass

for i in range(0,51,2):
    print(i)

# 0 Represents where to Start
# 51 Represents where to Stop
# 2 Represents Increment or Step

for i in range(0,51):
    print(i)

# 0 Represents where to Start
# 50 Represents where to Stop
# Imcrement of 1 is Implied

for i in range(51):
    print(i)

# Implies a start at 0
# 50 Represents where to Stop
# Imcrement of 1 is Implied

# *** Lists ***
# Prints the Index
person_one = [ "Rob", 45, "Purple", True, 3, 5 ]
for pineapple in range(len(person_one)):
    print(pineapple)

# Prints the Values of the list
person_one = [ "Rob", 45, "Purple", True, 3, 5 ]
for pineapple in range(len(person_one)):
    print(person_one[pineapple])

# *** Dictionaries ***
birds = {
    "Minnesota" : "Mosquito",
    "Illinois" : "Northern Cardinal",
    "Hawaii" : "Nene",
    "Vermont" : "Hermit Thrush",
    "Tennessee" : "bobwhite quail",
}

# *** States ***
# key can be changed to pineapple
# iterates through all the keys
for key in birds.keys():
    print(key)

# value can be changed to pineapple
# iterates through all the values
for pineapple in birds.values():
    print(pineapple)

# item can be changed to pineapple
# iterates through all the items
for item in birds.items():
    print(item)

for key, val in birds.items():
    if key == "Minnesota":
        print("Bring BUG Spray")
    print(key, val)
    print(key, " = ", val)

# *** Functions ***
def sum(num):
    print(num)
sum(6)

def birthday(age):
    age += 1
    return age
    print(age)
print(birthday(28))