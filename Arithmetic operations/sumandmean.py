"""
Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.

The program should function as follows:

Number 1: 2
Number 2: 1
Number 3: 6
Number 4: 7
The sum of the numbers is 16 and the mean is 4.0
"""

#Solution
num = 0
num += int(input("Number 1:"))
num += int(input("Number 2:"))
num += int(input("Number 3:"))
num += int(input("Number 4:"))

mean = num/4

print(f"The sum of the numbers is {num} and the mean is {mean}")
