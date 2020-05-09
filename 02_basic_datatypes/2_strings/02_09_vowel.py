'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
say = input("Put in a string here: ")
seta = 0
sete = 0
seti = 0
seto = 0
setu = 0

for ia in say:
            if(ia == "a" or ia == "A"):
                seta = seta + 1

for ie in say:
            if(ie == "e" or ie == "E"):
                sete = sete + 1

for ii in say:
            if(ii == "i" or ii == "I"):
                seti = seti + 1

for io in say:
            if(io == "o" or io == "O"):
                seto = seto + 1

for iu in say:
            if(iu == "u" or iu == "U"):
                setu = setu + 1

print(" Number of A : " + str(seta) + "\n Number of E: " + str(sete) + "\n Number of I: " + str(seti) +
      "\n Number of O: " + str(seto) + "\n Number of U: " + str(setu))
