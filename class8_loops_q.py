#1/10 class

# number of factors
'''num = int(input("tell your number:- "))
count = 0
for i in range(1,num+1):
    if num%i == 0: 
         count += 1         
print(f"the num of factors are {count}")'''

# prime num of not
'''
num = int(input("tell your number:- "))
count = 0
for i in range(1,num+1):
    if num%i == 0: 
         count += 1
print(f"the num of factors are {count}")
if count == 2:
     print(f"{num} is a prime number")
else :
     print(f"{num} is a composite number") '''

#other method of prime
'''num = int(input("enter a number: - ")) 6
#1 and number itself are factors.
for i in range(2,num):  2,3,4,5
     if num % i == 0: 6%2 == 0 true
          print(f"{num} is a composite number.")
          break
else:
     print(f"{num} is a prime number.")'''

# counting number of alphabets uppercase or lowercase

name = "AbhiSHEK"
count1 = 0
count2 = 0
for i in name:
    if i.isupper():
        count1 += 1
    else:
        count2 += 1
print(f"upper is : {count1}")
print(f"lower is : {count2}")