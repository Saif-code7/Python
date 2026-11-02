# loops - automating a task

# for loop - end point is known 
# while loop - based on condition as end point is not known

# for loop :

# a = range(1,21,1)    # start , stop , steps

# for i in a:   # in ka mtlb loops start ho gya 
#     print(i)

# for i in range(10,81,1):
#     print(i)

# for j in range(-52,40,1):
#     print(j)

# for k in range(100,-101,-1):
#     print(k)

# '''
# for i in range(1,11,1):
#     print(i*7)
#     '''

n = int(input("tell your number:- "))
for i in range(n,n*10+1,n):
    print(i)

#30/09
# take an n print natural numbers upto n
'''
n = int(input("tell your number:- "))
for i in range(1, n+1,1):
    print(i,"",end=""); '''

# take n as the input and print numbers from n to 1
'''
n = int(input("tell your number:- "))
for i in range(n, 0,-1):
    print(i,"",end=""); '''

# take n as input and print the sum of
'''
n = int(input("enter your number:- "))
sum = 0
for i in  range(1,n+1):
    sum = sum +i

print(sum) '''

# take input n and print the factorial
'''
n = int(input("enter your number:- "))
fact = 1
for i in range(1,n+1):
    fact = fact *i
print(fact) '''

#  take n as input and print factors of n
# '''num = int(input("tell your number:- "))

'''num = int(input("tell your number:- "))

for i in range(1,num+1):
    if num%i==0:
        count = 0
        for j in range(1,i+1):
            if i%j == 0:
                count += 1
        if count == 2:
            print(i)'''













