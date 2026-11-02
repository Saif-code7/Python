'''**Q3. Monthly Savings Analysis**

A person records the amount saved on **7 different days**.

Write a program to calculate the **total savings** and 
determine how many days the savings were **greater than ₹500**.
'''

sumSave = 0
countDays = 0
for i in range(1,8):
    savings = int(input("enter your savings sir:- "))
    sumSave += savings
    if savings > 500:
        countDays += 1
print(f"Sir your whole week savings are :- {sumSave}")
print(f"number of days where savings were greater than 500 :- {countDays}")
