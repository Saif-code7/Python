"""## Q6. Shopping Delivery Charge
Take the shopping amount as input.
Calculate the delivery charge:
- Amount below ₹500 → ₹50 delivery charge
- Amount from ₹500 to ₹999 → ₹30 delivery charge
- Amount ₹1000 or above → Free delivery
Print the final amount including the delivery charge.
**Example:**
Enter shopping amount: 800
Output:
Final Amount = ₹830
"""
amount = float(input("Enter shopping amount:- "))
if amount < 500:
    amount = amount + 50
    print(amount)
elif amount <1000:
    amount = amount + 30 
    print(amount)
else:
    print(amount)