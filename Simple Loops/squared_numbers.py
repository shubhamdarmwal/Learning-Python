"""
Writa a program which asks the user to type in a number and then prints out the number squared.
This continues until the user types in -1.

Running the program could look like this:
Please type in a number, -1 to quit: 2
4
Please type in a number, -1 to quit: 4
16
Please type in a number, -1 to quit: 10
100
Please type in a number, -1 to quit: -1
Thanks and bye!
"""
while True:
    number = int(input("Please type in a number, -1 to quit: "))

    if number == -1:
        break
    print(number ** 2)

print("Thanks and bye!")
