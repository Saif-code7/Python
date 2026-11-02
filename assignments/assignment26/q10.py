'''**Q10. Check Shopping Amount**

Take shopping amount as input. If the amount is 1000 or more, print Free Delivery, otherwise print Delivery Charges.

**Input:** 1200

**Output:** Free Delivery
'''

amount = float(input("enter amount :- "))
if amount >= 1000:
    print("Free Delivery")
else:
    print("Delivery Charges")