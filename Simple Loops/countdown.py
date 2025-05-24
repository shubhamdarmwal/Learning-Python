"""
Write a program that prints out a countdown.

That should print out:
Countdown!
5
4
3
2
1
Now!
"""
number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number <= 0:
    break
print("Now!")
