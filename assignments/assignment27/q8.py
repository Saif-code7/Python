'''## Q8. Electricity Bill

Take the number of units consumed as input.
Calculate the electricity bill according to these rules:
- Up to 100 units → ₹5 per unit
- 101 to 200 units → ₹7 per unit
- Above 200 units → ₹10 per unit
Print the total bill.
**Example:**
Enter units: 150
Output:
Electricity Bill = ₹1050
'''
units = int(input("Enter units: "))
if units <= 100:
    print(f"Electricity Bill = ${units*5}")
elif units <= 200:
    print(f"Electricity Bill = ${units*7}")
else:
    print(f"Electricity Bill = ${units*10}")