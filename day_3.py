# For loops, range()
def counter(number):
    for i in range(number):
        print(i)

number = 3
counter(number)

# Arrays
def counter(list):
    for value in list:
        print(value)

arr = [0, 1, 2]
counter(arr)

# Strings as arrays
def counter(string):
    for character in string:
        print(character)

string = "abcd"
counter(string)

# Dictionaries as strings, number, boolean
def counter(dict):
    for name in dict:
        value = dict[name]
        print(name, value)

dict = {
    "Num1": 0,
    "Num2": 1,
    "Num3": 2,
    "Array": [0, 1, 2],
    "String": "abcd",
    "Boolean": True,
}
counter(dict)