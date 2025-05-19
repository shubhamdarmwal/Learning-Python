"""
Write a program that allows the user to proceed only if they type in the correct PIN 1234.

Sample output
Please type in your PIN: 0000
Incorrect...try again
Please type in your PIN: 9999
Incorrect...try again
Please type in your PIN: 1234
Correct PIN entered!
"""
while True:
    code = input("Please type in your PIN: ")
    if code == "1234":
        break
    print("Incorrect...try again")

print("Correct PIN entered!")
