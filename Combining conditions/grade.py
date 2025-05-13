"""
The table below outlines the grade boundaries on a certain university course.
Please write a program which asks for the amount of points received and then prints out the grade attained according to the table.

points	grade
< 0	    impossible!
0-49	  fail
50-59	  1
60-69	  2
70-79	  3
80-89	  4
90-100	5
> 100	  impossible!

Some examples:
How many points [0-100]: 37
Grade: fail

How many points [0-100]: 76
Grade: 3

How many points [0-100]: -3
Grade: impossible!
"""
point = int(input("How many points [0-100]: "))

if point < 0 or point > 100 :
    print("Grade: impossible!")
elif point <= 49 :
    print("Grade: fail")
elif point <= 59 :
    print("Grade: 1")
elif point <= 69 :
    print("Grade: 2")
elif point <= 79 :
    print("Grade: 3")
elif point <= 89 :
    print("Grade: 4")
else :
    print("Grade: 5")

