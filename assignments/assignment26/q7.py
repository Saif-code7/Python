'''**Q7. Check Number Divisible by 5**

Take input of a number and check whether it is divisible by 5 or not.

**Input:** 20

**Output:** Divisible by 5
'''
num = float(input("enter number :- "))
if num %5 ==0:
    print(f"{num} is divisible by 5")
else:
     print(f"{num} is not divisible by 5")