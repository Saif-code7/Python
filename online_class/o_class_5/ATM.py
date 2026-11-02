
"""
# Q. ATM Machine Simulation
#
# Write a Python program to simulate an ATM machine with the following rules:
#
# 1. PIN Verification:
#    - Default correct PIN is 1234.
#    - User gets a maximum of 3 attempts to enter the correct PIN.
#    - If entered incorrectly 3 times, print "Card Blocked! Please contact your bank." and terminate.
#
# 2. Main Menu (runs continuously until user exits):
#    - Initial Account Balance = ₹5000. 
#    - If PIN is correct, show the menu options:
#        1. Check Balance
#        2. Deposit Cash
#        3. Withdraw Cash
#        4. Exit
#
# 3. Operations:
#    - Option 1: Display the current balance.
#    - Option 2: Ask for deposit amount, add it to balance, and display updated balance.
#    - Option 3: Ask for withdrawal amount.
#                If amount <= balance, deduct and print "Withdrawal Successful".
#                Otherwise, print "Insufficient Balance!".
#    - Option 4: Print "Thank you for using our ATM. Have a nice day!" and exit the loop.
#    - Any other option: Print "Invalid Choice! Please choose 1 - 4."
"""

attempts = 3
main_menu = False
for i in range(0,3):
    pin = int(input("enter your pin"))
    if pin == 1234:
        main_menu = True
        break
    else:
        attempts -= 1
        if attempts >0:
            print(f"you have {attempts} left ")
        else:
            print("card blocked please contact your bank")

balance = 5000
if main_menu == True:
    
    # while main_menu == True:
        print("1. Check balance")
        print("2. Deposit cash")
        print("3. withdraw cash")
        print("4. Exit")
        choose = int(input("enter your choice:-"))
        
        if choose == 1:
            print(f"your balance is{balance} only")
        elif choose == 2:
            deposit = int(input("enter amount to deposit:-"))
            balance += deposit
            print(f"updated balance is :-  {balance}")
        elif choose == 3:
            withdarw = int(input("enter amount to withdraw:- "))
            if withdarw <= balance:
                balance -= withdarw
                print("Withdrawal Successful") 
            else:
                print("Insufficient balance")
        elif choose == 4:
            print("Thank you for using our ATM. Have a nice day!" )
            # break
        else:
            print("Invalid Choice! Please choose 1 - 4.")