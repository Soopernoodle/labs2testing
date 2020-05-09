'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

i = 3
ii = 3.33

print(float(i))
print(int(ii))

print(i // ii)

x, y = input ("Enter two values separated by a space: ").split()

out = int(x) * int(y)
print(out)

