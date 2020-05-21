'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

numonth = input("Put your number here for conversion: ")
numonth = int(numonth)

if numonth <= 12:
    if numonth == 1:
        print("January")
    elif numonth == 2:
        print("February")
    elif numonth == 3:
        print("March")
    elif numonth == 4:
        print("April")
    elif numonth == 5:
        print("May")
    elif numonth == 6:
        print("June")
    elif numonth == 7:
        print("July")
    elif numonth == 8:
        print("August")
    elif numonth == 9:
        print("September")
    elif numonth == 10:
        print("October")
    elif numonth == 11:
        print("November")
    elif numonth == 12:
        print("December")
else:
    print("Other")