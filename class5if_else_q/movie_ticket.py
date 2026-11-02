"""
# Q4. Movie Ticket Discount

A cinema gives discounts based on the age of the customer.

If the customer's age is below 5, the ticket is FREE.
If the age is between 5 and 17, the ticket costs ₹100.
If the age is between 18 and 59, the ticket costs ₹200.
If the age is 60 or above, the ticket costs ₹120.

 Take the customer's age as input and print the ticket price.


Example:
Enter age: 65
Output: Ticket Price = ₹120

"""

age = int(input("enter age : "))
if age < 5 :
    print("ticket is free")
elif  age < 18:                                #maintaining order is very imp in these types of q
    print("Ticket price = $100")
elif age  < 60:
    print("Ticket price = $200")
else:
    print("price is = $120")

# if age < 5 :
#     print("ticket is free")
# elif age >=5 and age <=17:
#     print("Ticket price = $100")
# elif age >=18 and age <=59:
#     print("Ticket price = $200")
# else:
#     print("price is = $120")
    
