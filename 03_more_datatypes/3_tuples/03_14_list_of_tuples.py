'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
result_list = []
gotit = input("Please input your string here: ").split()

for x in gotit:
    result_list.append(tuple(x))

print(result_list)


