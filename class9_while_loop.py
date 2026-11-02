"""
FOR LOOP
KAHAN SE JANA HAI -> KAHA TA JANA HAI -> KAISE JANA HAI
1-50
"""

"""
WHILE LOOP
kaha se jana hai -> kab tak jana hai -> kaise jana hai

while jab tak condition true hai:
    tab tak yeh code chalega.
"""
# ek se 10 tak print karna hai using 
"""
i = 1
while i<= 10:
    print(i)          # agr while false nhi hua toh infinite loop ban jayega
    i += 1 """

"""
i = 10
while i>=1:
    print(i)
    i = i-1  """


# keep asking user the passward until the password "Abhishek123#2@"

'''password =""    # assign 0 nhi krna hai intttt
while password != "Abhishek123#2@":
    password = input("enter passward:- ")
print("Access granted")'''

# print any table 
'''n = int(input("enter your number"))
i = 1
while i<=10:
    print(n*i)
    i+=1 '''

# n = int(input("enter the number"))
# i = n
# while(i<=(n*10)):
#     print(i)
#     i = i+n

# print even number sum  from 2 to 20
"""i = 2
sum = 0
while i<= 20:
    sum = sum +i
    i =i+2
print(sum) """

#other method
"""i = 2
sum = 0
while i<=20:
    if i%2 == 0:
        sum = sum+i
    i += 1
print(sum)"""

# print reverse number
'''n = int(input("enter a number:"))
r = 0
s =0
while(n>0):
    r = n%10
    count += 1
    s = s*10+r
    n = n//10
print(s)'''


# other method
'''n = int(input("enter number:- "))
while(n!=0):
    print(n%10,end="")
    n = n // 10'''

# count the reverse numbers
'''
n = int(input("enter a number:- "))
last = 0
s = 0
count = 0
while n!= 0:
    last = n%10
    count += 1
    s = s*10+ last
    n = n//10
print(count) '''

