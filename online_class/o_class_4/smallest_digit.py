n = int(input("enter your number:- "))
small = 9
while n>0 :
    ld = n%10
    if ld<small:
        small = ld
    n //= 10
print(small)