'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
first = input("Enter your first string: ")
seco = input("Enter your second string: ")
third = input("Enter your third string: ")

if len(first) > len(seco) and len(first) > len(third):
    print(str(len(first)) + " " + first)

if len(seco) > len(first) and len(seco) > len(third):
    print(str(len(seco)) + " " + seco)

if len(third) > len(first) and len(third) > len(seco):
    print(str(len(third)) + third)
