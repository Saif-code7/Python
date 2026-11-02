'''**Q4. Electricity Consumption**

A household records its electricity consumption for **7 days**.

Write a program to calculate the **total units consumed** and count how many days the 
consumption was **more than 10 units**
'''

sum = 0
count = 0
for i in range(1,8):
    units = float(input("enter units consumed:- "))
    sum += units
    if units > 10:
        count += 1
print(f"total units consumed= {sum}")
print(f"days when consumptions was more than 10 units = {count}")
