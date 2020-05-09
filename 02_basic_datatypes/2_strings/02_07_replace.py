'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

editing = input("Put something in here please: ")
sym = input ("Put a symbol in here please: ")
editing = editing.lower()
print(editing.replace("p", sym))