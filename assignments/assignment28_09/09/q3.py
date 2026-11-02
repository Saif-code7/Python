'''**Q3. Age and Permission**
Take age and permission (1 for Yes, 0 for No) as input.
First check whether age is 18 or above. If yes, 
check whether permission is 1. Print Allowed or Permission Required.
Input: 20, 1
Output: Allowed
'''
age = int(input("enter age:- "))
if age >= 18:
    per = int(input("enter permission:- "))
    if per == 1:
        print("Allowed")
    else:
        print("Permission Required")
else:
    print("Permission Required")


    '''

if age >=18:
    per = int(input("enter permission:- "))
    if per == 1:
        print("allowed")
    else:
        print("Permission Required")
else:
    print("Permission Required")



if age>=18:
    per = int(input("enter permisiion:-"))
    if per == 1:
        print("allowed")
    else:
        print("Permission Required")
else:
    print("Permission Required")



age= int(input("enter age:-"))
if age>=18:
    per = int(input("enter permission:-"))
    if per == 1:
        print("allowed")
    else:
        print("Permission Required")
else:
    print("Permission Required")



if age>=18:
    per = int(input("enter permission: - "))
    if per == 1:
        print("allowed")
    else:
        print("Permission Required")
else:
    print("Permission Required")

age = int(input("enter age :- "))
per = int(input("enter permission :- "))

if age >= 18 and per == 1:
    print("allowed")
else:
    print("Permission Required")

'''