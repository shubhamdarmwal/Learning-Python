"""
Write the program for the given output:

Please type in a number: 13
13 must be my lucky number!
Have a nice day!

Please type in a number: 101
The number was greater than one hundred
Now its value has decreased by one hundred
Its value is now 1
1 must be my lucky number!
Have a nice day!
"""
number = int(input("Please type in a number: "))
if number > 100 : 
    print("The number was greater than one hundred")
    number -= 100
    print("Now its value has decreased by one hundred")
    print("Its value is now", number)
print(f"{number} must be my lucky number!")
print("Have a nice day!")
