"""
Write the program checks whether a number is above zero, and then whether it is odd or even.
Please type in a number: 3
The number is odd

Please type in a number: 18
The number is even

Please type in a number: -4
The number is negative or zero
"""
number = int(input("Please type in a number: "))

if number > 0:
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative or zero")

"""
or can be written as:
number = int(input("Please type in a number: "))

if number > 0 and number % 2 == 0:
    print("The number is even")
elif number > 0 and number % 2 != 0:
    print("The number is odd")
else:
    print("The number is negative or zero")
"""
