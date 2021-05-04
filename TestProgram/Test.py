from math import *

first_name = "Melon"
first_name = first_name.upper()
age = 30
print("My name is " + first_name.lower() + ", and I am " + str(age) + " years old")
print(first_name.isupper())

# getting length of string
print(len(first_name))

# getting M's index
print(first_name[0].index("M"))

# replace Melon with Musk
print(first_name.replace("MELON", "Musk"))

print(age % 5)

print(ceil(3.5))