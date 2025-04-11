"""
Please write a program which asks the user for their name and year of birth. The program then prints out a message as follows:

What is your name? Frances Fictitious
Which year were you born? 1990
Hi Frances Fictitious, you will be 35 years old at the end of the year 2025
"""

#Solution
name = input("What is your name?")
year = int(input("Which year were you born?"))
age = 2025-year

print(f"Hi {name}, you will be {age} years old at the end of the year 2025")
