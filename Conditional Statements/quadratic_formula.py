"""
Please write a program for solving a quadratic equation of the form ax²+bx+c. 
The program asks for values a, b and c. It should then use the quadratic formula to solve the equation. The quadratic formula expressed with the Python sqrt function is as follows:

x = (-b ± sqrt(b²-4ac))/(2a).

You can assume the equation will always have two real roots, so the above formula will always work.

An example of expected behaviour:

Sample output
Value of a: 1
Value of b: 2
Value of c: -8

The roots are 2.0 and -4.0
"""

from math import sqrt

a = int(input("Value of a:"))
b = int(input("Value of b:"))
c = int(input("Value of c:"))

d =  sqrt((b*b) - (4*a*c))
x1 = (-b + d) / (2 * a)
x2 = (-b - d) / (2 * a)

print(f"The roots are {x1} and {x2}")
