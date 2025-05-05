"""
Please write a program which asks for the user's name. 
If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.
If the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.

Some examples:
Sample output
Please type in your name: Morty
I think you might be one of Mickey Mouse's nephews.

Sample output
Please type in your name: Huey
I think you might be one of Donald Duck's nephews.

Sample output
Please type in your name: Ken
You're not a nephew of any character I know of.
"""

name = input("Please type in your name:")
if name == "Morty" or name == "Ferdie" :
    print("I think you might be one of Mickey Mouse's nephews.")
elif name == "Huey" or name == "Dewey" or name == "Louie" :
    print("I think you might be one of Donald Duck's nephews.")
else :
    print("You're not a nephew of any character I know of.")
