"""
# Q6. Shopping Discount
#
# A shop gives discounts based on the total amount of the purchase.
#
# If the amount is less than ₹1000, there is no discount.
# If the amount is between ₹1000 and ₹4999, give a 10% discount.
# If the amount is ₹5000 or more, give a 20% discount.
#
# Take the purchase amount as input and calculate the final amount
# after applying the discount.
#
# Example:
# Enter purchase amount: 6000
# Output: Final Amount = ₹4800
#
"""

amount = int(input("enter amount :- "))
if amount < 1000:
    print(f" Final Amount = {amount}")
elif amount < 5000:
    amount = amount - 10/100*amount
    print(f" Final Amount = {amount}")
else:
    # amount = 20/100*amount
    print(f" Final Amount = {amount - 20/100*amount}")

