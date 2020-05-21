'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

tellme = input("Put in your number here: ")
if int(tellme) % 3 == 0:
    print(int(tellme) / 3)
else:
    print("You done messed up")