"""
# Q3. ATM Withdrawal
#
# Write a Python program to simulate 
#  simple ATM withdrawal.
#
# Assume that the correct PIN is 1234 
# and the account balance is ₹5000.
#
# Ask the user to enter their PIN.
# If the PIN is correct, ask them 
# to enter the withdrawal amount.
#


# If the withdrawal amount is less than or 
# equal to the balance,
# print "Withdrawal Successful".
# Otherwise, print "Insufficient Balance".
#
# If the PIN is incorrect, print "Incorrect PIN".
"""



pin = int(input("Enter pin :- "))
if pin ==  1234:
    amount = int(input("enter withdrawal amount :- "))
    if amount <= 5000:
        print("withdrawal successful")
    else:
        print("insufficient balance")
else:
    print("Incorrect PIN")

    #this q cannot be done by normal if else because amount enterd is always after pin
    #by nested 