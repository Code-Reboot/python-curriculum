# Operators
number = 1 + 2 - 3 * 4 / 5
print(number)

# Functions
def hello(name):
    print("Hello, " + name + "!")

name = input("What is your name?\n")
hello(name)

# Flow Statements
def password(input, code):
    if input == code:
        return "Unlocked"
    else:
        return "Locked"

code = "code camp"
input = input("What is the password?\n")
result = password(input, code)
print(result)