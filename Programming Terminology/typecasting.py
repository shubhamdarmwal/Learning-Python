"""
Please write a program which asks the user for a floating point number and then prints out the integer part and the decimal part separately. Use the Python int function.

You can assume the number given by the user is always greater than zero.

An example of expected behaviour:
Please type in a number: 1.34
Integer part: 1
Decimal part: 0.34
"""
num = float(input("Please type in a number:"))
num1 = num - int(num)

print(f"Integer part: {int(num)}")
print(f"Decimal part: {num1}")
