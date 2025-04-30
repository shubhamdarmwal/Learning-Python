"""
Write a program which determines the winner of a match.
This program should print out three different statements given different inputs:

Home goals scored: 4
Away goals scored: 2
The home team won!

Home goals scored: 0
Away goals scored: 6
The away team won!

Home goals scored: 3
Away goals scored: 3
It's a tie!
"""
goals_home = int(input("Home goals scored: "))
goals_away = int(input("Away goals scored: "))

if goals_home > goals_away:
    print("The home team won!")
elif goals_away > goals_home:
    print("The away team won!")
else:
    print("It's a tie!")
