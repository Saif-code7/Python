'''**Q5. Shopping Discount**
Take shopping amount and membership status (1 for Member, 0 for Non-member) as input.
First check whether the person is a member. If yes, check whether shopping amount is 1000 or more.
Print Discount Available or No Discount.
Input: 1500, 1
Output: Discount Available
'''
mem = int(input("Enter membership status:- "))
if mem == 1:
    amount = float(input("enter shopping discount:- "))
    if amount >= 1000:
        print("Discount Available")
    else:
        print("No Discount")
else:
    print("No Discount")

# if mem == 1:
#     amount = float(input("enter shopping amount:- "))
#     if amount >= 1000:
#         print("Discount Available")
#     else:
#         print("No Discount")
# else:
#     print("No Discount")


# if mem == 1:
#     amount = float(input("enter shopping amount:-"))
#     if amount>= 1000:
#         print("Discount Available")
#     else:
#         print("No Discount")
# else:
#     print("No Discount")

# if mem == 1:
#     amount = float(input("enter shoppimg amount :_"))
#     if amount>= 1000:
#         print("Discount available:-")
#     else:
#         print("No Discount")
# else:
#     print("No Discount")

if mem == 1:
    amount = float(input("enter shopping amount:- "))
    if amount >= 1000:
        print("Discount available:-")
    else:
        print("No Discount:- ")
else:
    print("No Discount:- ")