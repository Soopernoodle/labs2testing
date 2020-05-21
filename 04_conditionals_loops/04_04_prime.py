'''
Print out every prime number between 1 and 100.

'''
for x in range(1, 100):
    for i in range(2, x):
        if (x % i) == 0:
            break
    else:
        print(x)