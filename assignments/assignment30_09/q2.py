'''**Q2. Product Quality Inspection**

A factory inspects **10 products**. For each product, enter 1 if it passes inspection and 0 if it fails.

Determine the **number of products that passed and failed** the inspection.
'''


count1 = 0
count2 = 0
for i in range(1,11):
    ins = int(input("enter result:- "))

    if ins == 1:
        count1 += 1

count2 = 10 - count1
print(count1)
print(count2)