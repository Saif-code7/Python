# armstrong number or not


"""n = int(input("enter any number:- "))
sum = 0
length = len(str(n))                         # length sirf string ka niklta h or aise niklta hai
a = n
while n>0:
    ld = n%10
    
    sum = sum + (ld**length)
    n = n//10                                 # yeh q count se nhi hoga kabhi bhi
# print(sum)

if sum == a:
    print("Armstrong number")
else:
    print("not an armstrong number")"""


n = int(input("enter your number:- "))
ld = 0
s=0

temp = n
while n>0:
    ld = n%10
    s = s*10+ld
    n = n//10
print(s)

if s == temp:
    print("palindrome number")
else:
    print("not a palindrome number")

