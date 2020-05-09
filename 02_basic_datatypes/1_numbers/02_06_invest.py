'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
inv, rate, years = input("Please enter investment amount, interest rate percentage, "
                         "and number of years separated by space: ").split()
print("Your investment amount is " + inv)
print("Your investment rate percentage is " + rate)
print("Your number of years to invest is " + years)

later = int(inv) * float(rate) * int(years)

print("Your gains are " + str(later))