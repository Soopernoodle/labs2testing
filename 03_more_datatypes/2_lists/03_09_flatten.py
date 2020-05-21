'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
toplist = []
starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in starting_list:
    toplist += i

print(toplist)

