"""

If the number is positive, 
check whether it is greater than 10 or not.
If the number is not positive, 
print "Not Positive".

"""


a = int(input("enter a number: -  "))

if a>0:
    print("num is positive")
    if a>=10:
        print("and num>10")
    else:
        print("and num<10")
else:
    print("num is negative")