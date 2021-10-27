## var x = 3
## console.log(x)

# x = 2

## if ( x < 3 ) {
##     console.log(x)
## }

if x < 3:
    pass
    print(x)

##  Data Types

## Booleans

is_hungry = True

## Numbers

# Int
some_int = 42
# Float
some_float = 4.2
# Complex
complex = 3j

## Type
print(type(42))

age = "45"
print(int(age) + 1) # 46
print(age + str(1)) # 451

truck_name = "Rob's Pie Truck"
review = 3.14
print(truck_name)
print(len(truck_name))
print(f"{truck_name} from Chicago has {review} reviews")

# Composite Data Types

empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2])
# ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)
ninjas.pop()
print(ninjas)
ninjas.pop(0)
print(ninjas)

# List Slice
some_list = [ 3.14, 8.5, 14, 55, 24, 45 ]
first_three = some_list[0:3]
print(first_three)
first_three = some_list[2:5]
print(first_three)
last_three = some_list[4:]
print(last_three)

# Tuple
# Immutable
tuple_data = ('physics', 'chemistry', '1994', '1999')
tuple_data.append('Chicago')
print(tuple_data)

# Dictionary
some_dictionary = {
    # key : value pair
    "location" : "Chicago",
    "state" : "IL"
}

print(some_dictionary["location"] + some_dictionary["state"])