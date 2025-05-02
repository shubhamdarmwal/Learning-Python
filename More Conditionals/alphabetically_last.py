"""
Please write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

You can assume all words will be typed in lowercase entirely.

Some examples of expected behaviour:

Please type in the 1st word: car
Please type in the 2nd word: scooter
scooter comes alphabetically last.

Please type in the 1st word: zorro
Please type in the 2nd word: batman
zorro comes alphabetically last.

Please type in the 1st word: python
Please type in the 2nd word: python
You gave the same word twice.
"""
word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")

if word1 > word2:
    print(f"{word1} comes alphabetically last.")
elif word2 > word1:
    print(f"{word2} comes alphabetically last.")
else:
    print("You gave the same word twice.")
