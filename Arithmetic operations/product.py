"""
Write a program that asks the user for three numbers. The program then prints out their product, that is, the numbers multiplied by each other. 

An example of the expected execution of the program:

Please type in the first number: 2
Please type in the second number: 3
Please type in the third number: 5
The product is 30
"""

#Solution

number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number1 * number2 * number3

print("The product is", product)
