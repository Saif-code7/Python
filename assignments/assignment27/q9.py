'''## Q9. Bus Ticket Fare
Take the age of a passenger as input.
The normal ticket price is ₹200.
Apply the following rules:
- Age below 5 → Free
- Age 5 to 17 → 50% discount
- Age 18 to 59 → Full price
- Age 60 or above → 30% discount
Print the final ticket price.
**Example:**
Enter age: 65
Output:
Ticket Price = ₹140
'''
# normal ticket price is $100
age = int(input("Enter age: "))
if age < 5:
    print(f"ticket price = Free")
elif age < 18:
    print(f"ticket price = ₹{200 - (50/100*200)}")  #for rs - ctrl + alt + 4
elif age <60:
    print(f"ticket price = $200 ")
else:
    print(f"ticket price = ${200 - (30/100*200)}")