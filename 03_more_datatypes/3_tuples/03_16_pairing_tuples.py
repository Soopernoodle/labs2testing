'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''

samplist = [2, 5, 7, 98, 1, 45, 9, 3]
samplist.sort()
biglist = []
ending = samplist[-1]

if len(samplist) % 2:
    x = 0
    while x < len(samplist):
        biglist.append(tuple(samplist[ x, x + 1]))
        x += 2

else:
    x = 0
    while x < len(samplist):
        biglist.append(tuple(samplist[x, x + 1]))
        x += 2


print(biglist)