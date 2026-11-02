# n = int(input("enter your number:- "))
# count = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         count += 1
# print(count)

# num = int(input("enter your number:- "))
# count=0
# for i in range(1,n+1):
#     if n%i == 0:
#         count+= 1

# print(count)


# num = int(input("enter yoyr number:- "))
# count = 0
# for i in range(1,n+1):
#     if n%i == 0:
#       count +=1
# print(count)

# num = int(input("enter your number:- "))
# count =0
# for i in range(1,n+1):
#     if n%i == 0:
#         count+= 1
# print(count)

# num = int(input("enter your number:- "))
# count = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         count+= 1
# print(count)



# num = int(input("enter your number:- "))
# count = 0
# for i in range(1,num+1):
#     if num%i == 0:
#         count+= 1
# if  count == 2:
#     print("prime number")
# else:
#     print("composite number")


# n = int(input("enter your number:- "))
# for i in range(2,n):
#     if n%i == 0:
#         print("composite number")
#         break
# else:
#     print("prime number")


# n = int(input("enter your number:- "))
# for i in range(2,n):
#     if n%i == 0:
#         print("composite")
#         break
# else:
#     print("prime number")

# n = int (input("enter your number:- "))

# for i in range(2,n):
#     if n % i == 0:
#         print("composite number")
#         break
# else:
#     print("prime number")

# n = int(input("enter your number:- "))
# for i in range(2,n):
#     if n%i ==0:
#         print("composite number")
#         break
# else:
#     print("prime number")

# n = int(input("enter your number:- "))
# for i in range(2,n):
#     if n%i == 0:
#         print("composit enumber")
#         break
# else:
#     print("prime number")

# n = int(input("enter your number:= "))
# for i in range(2,n):
#     if n%i == 0:
#         print("composite ")
#         break
# else:
#     print("prime number")



# name = "SaifALI"
# upper = 0
# lower = 0
# for i in name:
#     if i.supper():
#         upper += 1
#     else:
#         lower += 1
# print(f"upper is : {upper}")
# print(f"lower is : {lower}")

# name = input("enter your number:- ")
# upper =0
# lower = 0
# for i in name:
#     if i.isupper():
#         upper += 1
#     else:
#         lower+= 1
# print(upper)
# print(lower)



# i = 1
# while i<=10:
#     print(i,end="")
#     i += 1

# i = 10
# while i>=1:
#     print(i,end="")
#     i -= 1

# password = input("enter your password: - ")

# while password != "SaifAli_123":
#     password = input("enter your password")
# print("Access Granted")


# n = int(input("enter the number:-  ")  )
# # i = 1
# # while(i <= (n*10)):   #1<  50
# #     print(i * n) #1 *5
# #     i = i+n-1 #2

# i = 1
# while(i<=10):
#     print(i*n)
#     i += 1

# i = 2
# sum = 0
# while i<=20:
#     if i % 2 == 0:
#         sum += i

#     i = i+1
# print(sum)
    

# num = int(input("enter your number:- "))
# last =0
# s = 0
# while num!=0:
#     last = num%10
#     s = s*10+last
#     num = num//10
# print(s)


# num = int(input("enter your number:- "))
# count =0 
# while(num>0):
#     print(num%10)
#     count += 1
#     num = num// 10
# print(count)



# n = int(input("enter any number:- "))

# def palindrome(n):
#     ld = 0
#     s=0
#     temp = n
#     while n>0:
#         ld = n%10
#         s=s*10+ld
#         n = n//10
#     if s == temp :
#         print("palindrome")
#     else:
#         print("not a palindrome")

# palindrome(n)

"""n = int(input("enter your number:- "))
on = n
sum = 0
while n>0:
    fact =1
    
    ld = n%10
    for i in range(1,ld+1):
        fact = fact*i
    sum = sum+fact
    n = n//10

print(sum)

if sum == on:
    print("strong number")
else:
    print("not")
"""


# def strong(n):
#     sum = 0 
#     on = n
#     ld = 0
    

#     while n>0:
#         fact = 1
#         ld = n%10
#         for i in range(1,ld+1):
#             fact = fact *i
#         sum = sum+fact
#         n = n//10
#     if sum == on:
#         return "strong"
#     else:
#         return"not"

# print(strong(145))


# n = int(input("enter your number:- "))

# a = 0
# b = 1


# for i in range(1,n+1):
#     print (a)
#     c = a+b
#     a=b
#     b =c


# def divisible(n):
#     count = 0
#     for i in range(1,n+1):
#         if i%3 == 0:
#             count += 1
#     return count

# print(divisible(15))



# def largest(n):
#     num1 = int(input('enter the number'))
#     for i in range(1,n):
#         mum =int(input("enter your number:- "))
#         if mum > num1:
#             num1 = mum
#     return num1

# print (largest(5))


# def pef(n):
#     sum = 0
#     on = n
#     for i in range(1,n):
#         if n%i == 0:
#             sum = sum + i
#     if sum == on:
#         return"perfect"
#     else:
#         return "not"

# print(pef(6))

# count1 = 0
# count2 = 0
# for i in range(1,8):
#     a = input("enter attendance")
#     if a == "p":
#         count1 += 1
#     else:
#         count2 +=1
# print(f" {count1}   and  {count2}")

# passs = 0
# fail = 0
# for i in range(1,11):
#     inp = int(input("enter inspection:- "))
#     if inp == 1:
#         passs += 1
#     else:
#         fail += 1
# print(passs)
# print(fail)

# n = int(input("enter:- "))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum += i
# print(sum)

# a = int(input())
# b = int(input())
# fact = 1
# for i in range(1,b+1):
#     fact = a *a
# print(fact)


# a = input()
# for a in "aeiouAEIOU":
#     print("vowel")
# else:
#     print("consonant")

# a = int(input("enter first number:- "))
# b = int(input("enter second number:- "))
# c = int(input("enter third number:- "))

# if a==b and b == c and a==c:
#     print("all are equal")
# elif a == b or b==c or a==c:
#     print("two numbers are equal")
# else:
#     print("none are eqaul")



# "Positive Even"      if the number is positive and even.
# "Positive Odd"       if the number is positive and odd.
# "Negative Even"      if the number is negative and even.
# "Negative Odd"       if the number is negative and odd.
# "Zero"               if the number is zero.
#

# n =int(input("enter the number:- "))

# if n>0 and n%2==0:
#     print("Positive Even")
# elif n>0 and n%2!=0:
#     print("Positive odd")
# elif n<0 and n%2==0:
#     print("Negative Even")
# elif n<0 and n%2!=0:
#     print("Negative odd")
# else:
#     print("zero")

"""
# Q4. Movie Ticket Discount

A cinema gives discounts based on the age of the customer.

If the customer's age is below 5, the ticket is FREE.
If the age is between 5 and 17, the ticket costs ₹100.
If the age is between 18 and 59, the ticket costs ₹200.
If the age is 60 or above, the ticket costs ₹120.

 Take the customer's age as input and print the ticket price.


Example:
Enter age: 65
Output: Ticket Price = ₹120

"""

# age = int(input("enter age:- "))
# if age<5:
#     print("ticket is free")
# elif age<18:
#     print("the ticket costs ₹100")
# elif age<60:
#     print("the ticket costs ₹200")
# else:
#     print("the ticket costs ₹120")

"""
# Q6. Shopping Discount
#
# A shop gives discounts based on the total amount of the purchase.
#
# If the amount is less than ₹1000, there is no discount.
# If the amount is between ₹1000 and ₹4999, give a 10% discount.
# If the amount is ₹5000 or more, give a 20% discount.
#
# Take the purchase amount as input and calculate the final amount
# after applying the discount.
#
# Example:
# Enter purchase amount: 6000
# Output: Final Amount = ₹4800
#
"""

# amt = float(input("enter your amount:- "))

# if amt < 1000:
#     print("no discount")
# elif amt<5000:
#     amt = amt -((10/100)*amt)
#     print(amt)
# elif amt>5000:
#     amt = amt -((20/100)*amt)
#     print(amt)


"""
# Q4. Number Game
#
# Take a number from the user.
# If the number is positive, 
# check whether it is even or odd.
#
# If the number is even, 
# check whether it is divisible by 4 or not.
#
# Print the appropriate result.
#
# Example:
# Enter number: 12
#
# Output:
# # Positive
# Even
# Divisible by 4
"""

# a = int(input("enter your number:- "))
# if a > 0:
#     print("positive")
#     if a%2 == 0:
#         print("even")
#         if a%4 ==0:
#             print("divisible by 4")
#         else:
#             print("not divisible by 4")
#     else:
#         print("odd")
# else:
#     print("negative")

# n = int(input("enter your number:- "))
# count = 0
# l2 = []
# for i in range(1,n):
#     if n%i ==0:
#         count += 1
#         l2.append(i)
# print(count)
# print(l2)


# n = int(input("enter your number:- "))
# # count = 0
# for i in range(2,n):
#     if n%i == 0:
#         print("composite")
#         break
# else:
#     print("prime")
       
# name = "AbhiSHEK"
# count_u = 0
# count_l = 0
# for i in name:
#     if i.isupper():
#         count_u += 1
#     else:
#         count_l += 1
# print(count_u)
# print(count_l)

# i = 2
# sum =0
# while i<=20:
#     if i%2 ==0:
#         sum += i
#     i +=1
# print(sum)

# n =int(input())
# while n>0:
#     print(n%10)
#     n //= 10

# n = int(input("enter your number: "))
# length = len(str(n))
# total =0
# on = n

# while n >0:
#     ld = n%10
#     total = total + (ld**length)
#     n = n//10

# if total == on:
#     print("armstrong")
# else:
#     print("fck off")
    

# n = int(input("enter your number: "))
# s = 0
# on = n
# while n>0:
#     ld = n%10
#     s = s*10+ld
#     n //= 10
# if s == on:
#     print("palin")
# else:
#     print("fuck uuuuu")

"""
# Q3. Check Strong Number 
#
# Take an integer N as input and
# check whether it is a Strong Number.
# A Strong Number is a number
# whose sum of factorials of its
# digits equals the original number.
#
# Example:
# Input: 145
# 1! = 1
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# Sum: 1 + 24 + 120 = 145
# Output: Strong Number
"""

# n = int(input("enter ur number:- "))
# sum = 0

# on = n
# while n >0:
#     ld = n%10
#     fact = 1
#     for i in range(1,ld+1):
#         fact = fact*i
#     sum = sum+fact
#     n = n//10
# if sum == on:
#     print("strong num")
# else:
#     print("no")

# n = int(input())

# a = 0
# b = 1
# c = 0
# while n>0:
#     print(a)
#     c = a+b
#     a = b
#     b = c

# Q8. Print All Numbers Ending with 7 from 1 to N
#
# Take an integer N as input and 
# print all numbers from 1 to N that end with the digit 7.
#
# Example:
# Input: 40
# Output:
# 7 17 27 37

# n = int(input())
# l2 = []
# for i in range(1,n+1):
#     if i %10 == 7:
#         l2.append(i)
# print(l2)

"""
# Q. Digit Frequency

# Take an integer N as input and count how many times
# each digit from 0 to 9 occurs in the number.
#
# Example:
# Input: 122333
#
# Output:
# 1 -> 1
# 2 -> 2
# 3 -> 3
"""

# n = int(input("enter your number:- "))

# for i in range(0,10):
#     count = 0
#     temp = n
#     while temp>0:
#         ld = temp%10
#         if ld == i:
#             count += 1
#         temp = temp//10
#     if count >0:
#         print(f"{i} = {count}")


# arr = [ 10,20,30,40,50]
# n = len(arr)
# mid = n//2
# for i in range(mid):
#     arr[i] , arr[n-i-1]  =  arr[n-i-1] ,arr[i]
# print(arr)


# arr = [10, -5, 20, -3, 0, 8]
# l1 = []
# l2 = []
# for i in arr:
#     if i>0:
#         l1.append(i)
#     elif i<0:
#         l2.append(i)
# print(l1)
# print(l2)

# arr = [ 10,-5,20,-3,0,8]
# l_evn =[]
# l_odd =[]

# for i in range(0,len(arr) ):
#     if arr[i]>0:
#         l_evn.append(arr[i])
#     elif arr[i]<0:
#         l_odd.append(arr[i])

# print(l_evn)
# print(l_odd)


# arr = [2, 96, 69, 77, 145, 20]
# large = arr[0]
# n = len(arr)
# index = 0
# for i in range(n):
#     if arr[i] > large:
#         large = arr[i]
#         index = i
# print(f"Max element = {large}")
# print(f"found at {index} index")

# arr = [2, 96, 69, 77, 145, 20]
# min = arr[0]
# index = 0
# for i in range(1,len(arr)):
#     if arr[i] < min:
#         min = arr[i]
#         index = i
# print(f"Min element = {min} found at {index} index")


# arr = [2, 96, 69, 77, 145, 20]
# large = arr[0]
# sl = 0
# for i in range(1,len(arr)):
#     if arr[i] > large:
#         sl = large
#         large = arr[i]
#     elif arr[i] > sl and arr[i] !=large:
#         sl = arr[i]
# print(f"Second greatest element = {sl}")


# arr = [10, 20, 30, 40, 50]
# check = arr[0]
# n = len(arr)
# count = 0
# for i in range(0,n):
#     if arr[i] >arr[i-1]:
#         count += 1
# if count == n:
#     print("list is sorted")


# arr = [2,3,3,2]
# arr2 = str(arr)
# summ  =  ""
# is_rev = True
# n = len(arr2)
# for i in range(n//2):
#     if arr2[i] != arr2[n-i-1]:
#         is_rev = False
# if is_rev :
#     print("list is palindrome")
# else:
#     print("list is not palindrome")



# arr = [2,3,3,2]
# arr2 = "".join(map(str,arr))
# og = arr2
# rev  = ""

# for i in range(len(arr2)):
#     rev = arr2[i]+ rev

# if rev == og:
#     print("list is palindrome")
# else:
#     print("list is not palindrome")


# arr = [1,2,4,5]
# n = len(arr)+1
# og_sum = (n*(n+1))//2
# real_sum = 0
# for i in arr:
#     real_sum += i
# missing = og_sum - real_sum
# print(missing)


# arr = [10, 20, 30, 40, 50]
# is_sort = True

# for i in range(len(arr)-1):
#     if arr[i] > arr[i+1]:
#         is_sort = False
# if is_sort:
#     print("sorted")
# else:
#     print("not")


# arr = [10, 20, 30, 40, 50]
# count = 0
# n = len(arr)

# for i in range(1,len(arr)):
#     if arr[i] > arr[i-1]:
#         count += 1
# if count == n-1:
#     print("sort")
# else:
#     print("not")

# arr = [2, 3, 15, 15, 3, 2]
# n = len(arr)
# mid = n//2
# ispalin = True
# for i in range(mid):
#     if arr[i]  !=  arr[n-i-1]:
#         ispalin = False
# if ispalin:
#     print("palin")
# else:
#     print("not")
        

# arr = [64,34,25,12,22,11,9]
# for i in range(len(arr)):
#     for j in range(i):
#         if arr[j] > arr[j+1]:
#             arr[j] , arr[j+1] = arr[j+1] , arr[j]
# print(arr) 



"""
# Find the Pair with the Given Sum
#
# Find all pairs of elements whose sum equals a given target.
#
# Example:
# Input: [2, 4, 3, 5, 7, 8]
# Target: 10
#
# Output:
# (2, 8)
# (3, 7)
"""

# ld = [2, 4, 3, 5, 7, 8]
# n = len(ld)
# target = 10
# for i in range(n):
#     for j in range(i+1,n):
#         if ld[i] + ld[j] == target:
#             print(f"({ld[i]}, {ld[j]})")

# ld = [2, 4, 3, 5, 7, 8]
# target = 10
# for i in range(len(ld)):
#     for j in range(i+1,len(ld)):
#         if ld[i] + ld[j] == target:
#             print(ld[i],ld[j])

# ld = [2, 4, 3, 5, 7, 8]
# n = len(ld)
# target = 10
# for i in range(n):
#     for j in range(i+1,n):
#         if ld[i] + ld[j] == target:
#             print(ld[i], ld[j])


# ld = [2, 4, 3, 5, 7, 8]
# n = len(ld)
# target = 8
# for i in range(n):
#     for j in range(i,n):
#         if ld[i] +ld[j] == target:
#             print(ld[i],ld[j])

# ld = [2, 4, 3, 5, 7, 8]
# for i in range(len(ld)):
#     for j in range(i,len(ld)):
#         if ld[i] + ld[j] == 11:
#             print(ld[i] , ld[j])

# ld = [2, 4, 3, 5, 7, 8]
# targte = 10
# n = len(ld)
# for i in range(n):
#     for j in range(i+1,n):
#         if ld[i] +ld[j] == targte:
#             print(ld[i],ld[j])

# arr =[2, 4, 3, 5, 7, 8]
# n = len(arr)

# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i] + arr[j] == 10:
#             print(arr[i] , arr[j])

# arr = [2, 4, 3, 5, 7, 8]
# for i in range(n):
#     for j in range(i,n):
#         if arr[i] + arr[j]== 10:
#             print(arr[i] , arr[j])


# arr =   [64, 34, 25, 12, 22, 11, 9]
# n = len(arr)
# for i in range(n):
#     for j in range(n-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1] , arr[j]
# print(arr)


# arr = [10, 20, 30, 40, 50]
# m = len(arr)
# sub = [20, 30, 40]
# n =len(sub)
# for i in range(m-n+1):
#     if arr[i:i+m] == sub:
#         print("sublist found")
#         break
# else:
#     print("not found")

# arr = [1,2,3,4,5]
# k = int(input())
# for i in range(k%(len(arr))):
#     last = arr.pop()
#     arr.insert(0,last)
# print(arr)

# arr = [1,2,3,4,5]
# k = 2
# k = k%5
# n = len(arr)
# for i in range(k):
#     last = arr.pop()
#     arr.insert(0,last)
# print(arr)

# arr = [1,2,3,4,5]
# k = 2
# k = k%len(arr)
# for i in range(k):
#     last = arr.pop()
#     arr.insert(0,last)
# print(arr)

# arr = [1,2,3,4,5]
# k = 2
# k = k%len(arr)
# for i in range(k):
#     last = arr.pop()
#     arr.insert(0,last)
# print(arr)

# arr = [1,2,3,4,5]
# k = 2
# k = k%len(arr)
# for i in range(k):
#     last = arr.pop()
# #     arr.insert(0,last)
# # print(arr)

# # arr = [1,2,3,4,5]
# # k = 2
# # k = k%len(arr)
# # for i in range(k):
# #     last = arr.pop()
# #     arr.insert(0,last)
# # print(arr)


# arr = [1, 2, 3, 2, 4, 1, 5]
# n = len(arr)
# l2 =[]
# for i in range(n):
#     count = 1
#     for j in range(i+1,n):
#        if arr[i] == arr[j]:
#            count += 1
#     if count>1:
#         l2.append(arr[i])
# print(l2)


# arr = [1, 2, 3, 2, 4, 1, 5]
# n = len(arr)
# l2 = []
# for i in range(n):
#     count = 1
#     for j in range(i+1,n):
#         if arr[i] == arr[j]:
#             count += 1
#     if count > 1:
#         l2.append(arr[i])
# print(arr)


# arr = [1, 2, 3, 2, 4, 1, 5]
# n = len(arr)
# l2  =  []

# for  i in range(n):
#     count  = 1
#     for j in range(i+1,n):
#         if arr[i] == arr[j]:
#             count += 1
#     if count > 1:
#         l2.append(arr[i])
# print(l2)

# arr = [1, 2, 3, 2, 4, 1, 5]
# n = len(arr)
# l2 = []

# for i in range(n):
#     count = 1
#     for j in range(i+1,n):
#         if arr[i] == arr[j]:
#             count += 1
#     if count > 1:
#         l2.count(arr[i])
# print(l2)

# arr = [1, 2, 3, 2, 4, 1, 5]
# n = len(arr)

# l2 = []
# for i in range(n):
#     vount = 1
#     for j in range(i+1,n):
#         if arr[i] == arr[j]:
#             vount += 1
#     if vount>1:
#         l2.append(arr[i])
# print(arr)

# arr = [1, 2, 3, 2, 4, 1, 5]
# l2 = []
# for i in range(len(arr)):
#     if arr[i] not in l2:
#         l2.append(arr[i])
# print(l2)


# arr1 = [1,4,7,10]
# arr2 = [2,3,8,9]
# n = len(arr1)
# m = len(arr2)
# i = 0
# j = 0
# ans = []

# while i<n and j< m:
#     if arr1[i] < arr2[j]:
#         ans.append(arr1[i])
#         i +=1
#     else:
#         ans.append(arr2[j])
#         j += 1
# while i < n:
#     ans.append(arr1[i])
#     i += 1
# while i < m:
#     ans.append(arr2[j])
#     j += 1
# print(ans)


# arr1 = [1,4,7,10]
# arr2 = [2,3,8,9]

# n = len(arr1)
# m = len(arr2)
# i = 0
# j = 0
# ans = []

# while i<n and j < m:
#     if arr1[i] < arr2[j]:
#         ans.append(arr1[i])
#         i += 1
#     else:
#         ans.append(arr2[j])
#         j += 1
# while i < n:
#     ans.append(arr1[i])
#     i += 1
# while j<m:
#     ans.append(arr2[j])
#     j += 1
# print(ans)



# arr1 = [1,4,7,10]
# arr2 = [2,3,8,9]
# n1 = len(arr1)
# n2 = len(arr2)
# ans = []

# for i in range(n1):
#     for j in range(n2):
#         if arr1[i] < arr2[j]:
#             ans.append(arr1[i])
#         else:
#             ans.append(arr2[j])
# while i < n1:
#     ans.append(arr1[i])
#     i += 1
# while j < n2:
#     ans.append(arr2[j])
#     j += 1

# print(ans)


"""name = "SHERYIANS"
for i in name[0:4:1]:
    print(i)

    
print(12 == 12 , 34 != 67 )


alpha = input("enter your alphabet:- ")
if alpha in "aeiouAEIOU":
    print("Vowel")
else:
    print("consonent")"""


# a = int(input("enter marks of first subject:= "))
# b = int(input("enter marks of sec subject:= "))
# c = int(input("enter marks of third subject:= "))
# if a >= 40 and b >= 40 and c >= 40:
#     print("pass")
# else:
#     print("fail")



"""Your program should check:
- If all three numbers are equal, print "All are equal".
- If any two numbers are equal, print "Two numbers are equal".
- If all three numbers are different, print "All are different".

Example:
 Enter first number: 10
 Enter second number: 20
 Enter third number: 30

 Output:
 Two numbers are equal
"""


# a  =  int(input("enter your first number:- "))
# b  =  int(input("enter your second number:- "))
# c  =  int(input("enter your third number:- "))
# if a == b and b == c and a==c:
#     print("All are equal")
# elif a == b or b==c or a==c:
#     print("Two numbers are equal")
# else:
#     print("All are different")


# age = int(input("whats your age:- "))
# if age<5:
#     print("ticket is free")
# elif age<18:
#     print("the ticket costs ₹100")
# elif age<60:
#     print("the ticket costs ₹200")
# else:
#     print("the ticket costs ₹120")

"""# Your program should check the number and print:
#
# "Positive Even"      if the number is positive and even.
# "Positive Odd"       if the number is positive and odd.
# "Negative Even"      if the number is negative and even.
# "Negative Odd"       if the number is negative and odd.
# "Zero"               if the number is zero.

"""
# n = int(input("enter your number:- "))
# if n>0 and n%2==0:
#     print("Positive Even")
# elif n>0 and n%2 != 0:
#     print("Positive Odd")
# elif n<0 and n%2 == 0:
#     print("negative even")
# elif n<0 and n%2 != 0:
#     print("negative Odd")
# else:
#     print("zero")

"""# A shop gives discounts based on the total amount of the purchase.
#
# If the amount is less than ₹1000, there is no discount.
# If the amount is between ₹1000 and ₹4999, give a 10% discount.
# If the amount is ₹5000 or more, give a 20% discount.
#
"""

# amt = float(input("enter your amount:- "))
# if amt <1000:
#     print("no discount")
# elif amt <5000:
#     amt = amt - (10*amt)/100
# else:
#     amt = amt - (20*amt)/100
# print(amt)
    

"""

If the number is positive, 
check whether it is greater than 10 or not.
If the number is not positive, 
print "Not Positive".

"""
# n = int(input())
# if n>0:
#     if n>10:
#         print("number is positive and greater than 10")
#     else:
#         print("number is positive and not greater than 10")
# else:
#     print("no is not positive")


"""
# Q2. Number Check
#
# Take a number from the user.
# If the number is even,
# check whether it is divisible by 4.
# If the number is odd, print "Odd Number".
"""

# n = int(input())
# if n%2==0:
#     print("no is even",end=" ")
#     if n%4==0:
#         print("and divisible by 4")
#     else:
#         print("and not divisible by 4")
# else:
#     print("odd")

"""
# Q5. Number Comparison
#
# Take two numbers from the user.
#
# If the first number 
# is greater than the second number,
# check whether the first number is even or odd.
#
# Otherwise, check whether 
# the second number is even or odd.
#
# Example:
# Enter first number: 15
# Enter second number: 10
#
# Output:
# First number is greater
# First number is odd
"""
# a = int(input("enter firdt number: -"))
# b =int(input("enter second number:- "))
# if a>b:
#     print(f"{a} is grater than {b}",end=" ")
#     if a%2==0:
#         print("and even")
#     else:
#         print("and odd")
# else :
#     print(f"{b} is grater than {a}",end=" ")
#     if b%2==0:
#         print("and even")
#     else:
#         print("and odd")

"""
# Q3. ATM Withdrawal
#
# Write a Python program to simulate 
#  simple ATM withdrawal.
#
# Assume that the correct PIN is 1234 
# and the account balance is ₹5000.
#
# Ask the user to enter their PIN.
# If the PIN is correct, ask them 
# to enter the withdrawal amount.
#


# If the withdrawal amount is less than or 
# equal to the balance,
# print "Withdrawal Successful".
# Otherwise, print "Insufficient Balance".
#
# If the PIN is incorrect, print "Incorrect PIN".
"""

# pin = input("enter pin:- ")
# balance = 5000
# if pin == "1234":
#     amt = float(input("enter withdrawal amount:- "))
#     if amt <= balance:
#         print("Withdrawal Successful")
#     else:
#         print("garib")
# else:
#     print("incorrect pin")

# num = int(input("enter your number:- "))
# count = 0
# for i in range(1,num+1):
#     if num%i == 0:
#         count += 1
# # print(count)
# if count == 2:
#     print("prime number")
# else:
#     print("not prime")


# num = int(input("enter your number:- "))
# for i in range(2,num):
#     if num%i == 0:
#         print("composite number")
#         break
# else:
#     print("prime number")

# name = "SADIEsink"
# countup =0
# countl = 0
# for ch in name:
#     if ch.isupper():
#         countup += 1
#     else:
#         countl += 1
# print(countup)
# print(countl)

'''Q1. Count Numbers Divisible by 3

Take an integer N as input and count how many numbers from 1 to N are divisible by 3.

Example:
Input: 15
Output: 5
'''

# n  =int(input("enter your number:-"))
# count = 0
# for i in range(1,n+1):
#     if i%3 ==0:
#         count +=1
# print(count)

'''Q2. Find the Largest Among N Numbers

Take N numbers as input and determine the largest number among them.

Example:
Input:
5
10                                # very very imp q can be done without arrays think!!!!!
25
7
18
12

Output:
25
'''

# n = int(input("enter your number:- "))
# large = int(input("enter expected number"))
# for i in range(n-1):
#     num = int(input("enter numbers:- "))
#     if num > large:
#         large = num
# print(large)


'''Q3.

Take N numbers as input. Calculate their average.

Example:
Input:
5
10
20
30
40
50
Output:
30.0
'''

# n = int(input("enter your number: -"))
# total = 0
# for i in range(n):
#     num = int(input("enter:- "))
#     total += num
# print(total/n)


# n = int(input("enter your number:- "))
# # on = n
# total = 0
# for i in range(1,n):
#     if n%i == 0:
#         total += i
# if total == n:
#     print("perfect number")
# else:
#     print("not")
    
'''**Q2. Student Result**
Take marks of two subjects as input. First check whether the student has
passed the first subject (33 or above). If yes, check whether the student
has passed the second subject. Print Pass or Fail.
Input: 45, 60
Output: Pass
'''

# m1 = int(input("enter marks of first subject:- "))
# m2 = int(input("enter marks of second subject:- "))
# if m1>=33:
#     if m2>=33:
#         print("pass")
#     else:
#         print("fail")
# else:
#     print("fail")

# n = int(input("enter your number:- "))
# for i in range(1,n+1):
#     print(i**2)


'''**Q1.Weekly Attendance Analysis**

An institution records the attendance status of a student for 
**7 consecutive days**. The status is entered as P for Present and A for Absent.

Write a program to determine the **total number of days the student was present and absent**.
'''
# countp = 0
# counta = 0
# for i in range(7):
#     attend = input("enter status:- ")
#     if attend in "pP":
#         countp += 1
#     elif attend in "aA":
#         counta += 1
# print(f"present = {countp}")
# print(f"absent = {counta}")

'''**Q2. Product Quality Inspection**

A factory inspects **10 products**. For each product, enter 1 if it passes inspection and 0 if it fails.

Determine the **number of products that passed and failed** the inspection.
'''
# pas = 0
# fail = 0

# for i in range(10):
#     inp = int(input("enter:- "))
#     if inp == 1:
#         pas += 1
#     else:
#         fail += 1
# print(pas)
# print(fail)

'''**Q3. Monthly Savings Analysis**

A person records the amount saved on **7 different days**.

Write a program to calculate the **total savings** and 
determine how many days the savings were **greater than ₹500**.'''

# saving = 0
# count =0 
# for i in range(7):
#     amt = int(input("enter amout saved:- "))
#     if amt>500:
#         count += 1
#     saving += amt
# print(saving)
# print(count)

'''**Q5. Attendance Eligibility**

A student has **10 classes**. For every class, enter P for Present and A for Absent.

Calculate the students **attendance percentage** and display whether the student has **75% or more attendance**.
'''
# for i in range(10):
#     a = input("enter ")


"""Q1. Difference between Sum of Odd numbers and Sum of Even Numbers

Take an integer N as input. Calculate the sum of even numbers
and the sum of odd numbers from 1 to N, then find the difference between the two sums.

Example:
Input: 5
Output: 3
"""
# sum_evn = 0
# sum_odd = 0
# n = int(input("enter your number:- "))
# for i in range(1,n+1):
#     if i%2==0:
#         sum_evn += i
#     else:
#         sum_odd += i
# print(sum_evn-sum_odd)

"""Q2. Difference Between Largest and Smallest
+Take N numbers as input and calculate the difference between the largest and smallest number.
Example:
Input:
5
10
25            
7
18
12
Output:
2"""



# n = int(input("enter your number:- "))
# small = int(input("enter expected number:-"))
# large = small
# for i in range(n-1):
#     num = int(input("enter your numbers_ "))
#     if num > large:
#         large = num
#     elif num < small:
#         small = num
# print(large)
# print(small)
# print(large - small)

"""Q3. Find the Smallest Number

Take N numbers as input and determine the smallest number among them.

Example:
Input:
5
18
7
25
3
12

Output:
3
"""
# n =  int(input("enter your number:- "))
# smALL = int(input("ENTER"))
# for i in range(n-1):
#     num = int(input("enters:- "))
#     if num < smALL:
#         smALL = num
# print(smALL)

"""Q4. Count Numbers Having Digit 0

Take N integers as input and count how many of them contain the digit 0.

Example:
Input:
5
10
25
30
17
40

Output:
3
"""
# n = int(input())
# count = 0
# for i in range(n):
#     num = input()
#     if "0" in num:
#         count +=1

# print(count)

"""Q1. Reverse a Number

Take an integer N as input and print its reverse.

Example:
Input: 12345
Output: 54321
"""

# num  =int(input("enter your number:- "))
# s = 0
# on = num
# while num>0:
#     ld = num%10
#     s = s*10+ld
#     num //= 10
# if s == on:
#     print("palindrome")
# else:
#     print("not")


"""Q3. Count Digits Greater Than 5

Take an integer N as input and count how many digits in the number are greater than 5.

Example:
Input: 583721
Output: 2
"""

# n = 583721
# # n = str(n)
# count =0
# while n >0:
#     if n%10 > 5:
#         count += 1
#     n = n//10
# print(count)

# n = 234
# pro = 1
# while n>0:
#     ld = n%10
#     pro *= ld
#     n //= 10
# print(pro)

# n = 5831
# n = str(n)
# for ch in n:
#     if ch == "7":
#         print("present")
#         break
# else:
#     print("not")

# n =58371
# count = 0 
# while n>0:
#     ld = n%10
#     if ld == 7:
#         count += 1
#         break
#     n = n//10
# if count > 0:
#     print("present")
# else:
#     print("not ")

# n = int(input("enter your number:- "))
# count = 0
# while n>0:
#     ld = n%10
#     if ld %3 == 0:
#         count += 1
#     n = n//10
# print(count)

# n = int(input("enter: -"))
# s = 0
# while n >0:
#     ld = n%10
#     if ld != 9:
#         ld = 9
#     s = s*10+ld
#     n = n//10
# print(s)


"""Q8. Find the Second Largest Digit

Take an integer N as input and find the second largest digit present in N.

Example:
Input: 5832
Output: 5
"""

# n = 5832
# large = 0
# sl = 0
# while n>0:
#     ld = n%10
#     if ld > large :
#         sl = large
#         large = ld
#     elif ld>sl and ld != large:
#         sl = ld
#     n = n//10
# print(sl)
# n = 2486
# count = 0
# length = len(str(n))
# while n >0:
#     ld = n%10
#     if ld %2==0:
#         count += 1
#     n = n//10
# if count == length:
#     print("even")
# else:
#     print("not")

# def add(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c


# print(add(12,45,23))

"""Q2. Check Prime Number
Create a function is_prime() that takes a number and returns 
"Prime" if the number is prime, otherwise returns "Not Prime".

Example:
Input: 17
Output: Prime
"""

# def if_prime(n):
#     count = 0
#     for i in range(2,n):
#         if n%i ==0:
#             return "prime"
#     if count == 2:
#         return "prime"
#     else:
#         return "not prime"

# print(if_prime (7))

# def sum_dig(n):
#     total = 0
#     while n >0:
#         ld = n%10
#         total += ld
#         n = n//10
#     return total

# print(sum_dig(12345))

# def palin(n):
#     s = 0
#     on = n
#     while n >0:
#         ld = n%10
#         s =s*10+ld
#         n = n//10
#     if s == on:
#         return "palindrome"
#     else:
#         return "not"
# print(palin(1221))

# def count_even_odd(n):
#     evn = 0
#     odd =0
#     while n > 0:
#         ld = n%10
#         if ld%2==0:
#             evn += 1
#         else:
#             odd += 1
#         n = n//10
#     return evn , odd

# print(count_even_odd(34355635))

"""Q9. Check Armstrong Number
Create a function is_armstrong() that takes a number and 
checks whether it is an Armstrong number.

Example:
Input: 153
Output: Armstrong
"""


# def is_armstrong(n):
#     total  =  0
#     length = len(str(n))
#     on = n
#     while n >0:
#         ld = n%10
#         total = total + (ld**length)
#         n = n//10
#     if total == on:
#         return "Armstrong"
#     else:
#         return "not"
# print(is_armstrong(153))


"""Q1. Find the Smallest Element

Create a list of numbers and find the smallest element without using the min() function.

Example:

Input: [12, 5, 23, 8, 17]
"""
# l = [12, 5, 23, 8, 17]
# small = l[0]
# for i in range(len(l)):
#     if l[i] < small:
#         small = l[i]
# print(small)

# arr =[10, -5, 20, -8, 0, 7]
# pos = 0
# neg =0
# for i in arr:
#     if i >0:
#         pos += 1
#     elif i <0:
#         neg += 1
#     else:
#         continue
# print(pos)
# print(neg)

# arr = [10, 20, 30, 40]
# t = 0
# for i in arr:
#     t += i
# print(t/len(arr))

# arr =[2, 4, 2, 6, 2, 8]
# target = 2
# count = 0 
# for i in arr:
#     if i == target:
#         count+=1
# print(count)

"""Q5. Print Elements at Even Indices

Create a list and print the elements 
present at even indices (0, 2, 4, …).

Example:

Input: [10, 20, 30, 40, 50, 60]

Output: [10, 30, 50]
"""
# arr =[10, 20, 30, 40, 50, 60]
# l2 = []
# for i in range(len(arr)):
#     if i%2==0:
#         l2.append(arr[i])
# print(l2)

# arr =[10, 25, 15, 40, 30]
# large = arr[0]
# sl = arr[1]

# for i in arr:
#     if i>large:
#         sl = large
#         large = i
#     elif i > sl and i!=large:
#         sl = i
# print(sl)
# print(large)

# arr =[10, -5, 20, -8, 7]
# for i in range(len(arr)):
#     if arr[i] <0:
#         arr[i] = 0
# print(arr)

# arr =[10, 20, 30, 40, 50]
# l2 = []
# for i in range(len(arr)- 1,-1,-1):
#     l2 = arr[i]
#     print(l2)


"""**Q1. Separate Even and Odd Numbers**

Create a list of integers and separate the even and
odd numbers into two different lists.

**Example:**

- Input: [1, 2, 3, 4, 5, 6]
- Output:
    - Even: [2, 4, 6]
    - Odd: [1, 3, 5]
"""

# arr =[1, 2, 3, 4, 5, 6]
# evn = []
# odd = []
# for i in arr:
#     if i%2 == 0:
#         evn.append(i)
#     else:
#         odd.append(i)
# print(evn)
# print(odd)


"""**Q2. Remove Duplicates**

Create a list and remove duplicate
elements without using set().

**Example:**

- Input: [1, 2, 3, 2, 4, 1, 5]
- Output: [1, 2, 3, 4, 5]
"""
# arr =[1, 2, 3, 2, 4, 1, 5]
# l2 = []
# for i in range(len(arr)):
#     if arr[i] not in l2:
#         l2.append(arr[i])
# print(l2)

"""**Q3. Find the Index of an Element**

Create a list and find the index of a given 
element without using the index() method.

**Example:**

- Input: [10, 20, 30, 40, 50]
- Element: 30
- Output: 2
"""
# arr = [10, 20, 30, 40, 50]
# tar = 2
# index = 0
# for i in range(len(arr)):
#     if i == tar:
#         index = i
# print(index)

# arr = [10, 20, 30, 40, 50]
# arr[0] , arr[len(arr)-1]  = arr[len(arr)-1]  , arr[0]
# print(arr)

# arr1 = [1, 2, 3]  
# arr2 = [4, 5, 6]
# arr1.extend(arr2)
# print(arr1)

"""remove dublicate elements from the given list
ex = 
input: [1, 2, 3, 2, 4, 1, 5]
output: [1,2]
"""
# arr  = [1, 2, 3, 2, 4, 1, 5]
# n = len(arr)
# l2 = []
# for i in range(n):
#     count = 1
#     for j in range(i+1,n):
#         if arr[i] == arr[j]:
#             count += 1
#     if count > 1:
#         l2.append(arr[i])
# print(l2)

"""
# Q1. Count Numbers Divisible by Both 3 and 5
#
# Take an integer N as input and count how many numbers from 1 to N
# are divisible by both 3 and 5 (multiples of 15).
#
# Example:
# Input: 35
# Output: 2
# (Explanation: The numbers are 15 and 30. Total count = 2)
"""
# n = int(input())
# count = 0
# for i in range(1,n+1):
#     if i%3 == 0 and i%5 ==0:
#         count += 1
# print(count)


"""
# Q3. Check Strong Number 
#
# Take an integer N as input and
# check whether it is a Strong Number.
# A Strong Number is a number
# whose sum of factorials of its
# digits equals the original number.
#
# Example:
# Input: 145
# 1! = 1
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# Sum: 1 + 24 + 120 = 145
# Output: Strong Number
"""


# n =int(input())
# t = 0
# on = n
# while n >0 :
#     fact = 1
#     ld = n%10
#     for i in range(1,ld+1):
#         fact = fact*i
#     t = t+fact
#     n = n//10
# if on == t:
#     print("stong number")
# else:
    # print("not")


"""# Q6. Count Vowels in a String
#
# Take a string as input 
# and count how many vowels (a, e, i, o, u) are present in it.
# Check both lowercase and uppercase 
# vowels without using any string functions.
#
# Example:
# Input: "AbhiSHEK"
# Output:
# Total vowels: 3  (A, i, E)
"""
# s = input()
# count = 0
# for ch in s:
#     if ch in "aeiouAEIOU":
#         count += 1

# print(count)


# n = int(input("enter your number:- "))
# a = 0
# b = 1

# for i in range(1,n+1):
#     print(a)
#     c = a+b
#     a =b
#     b = c
    
# print(a)


"""
# Q7. Count Occurrences of a Character in a String
#
# Take a string and a target 
# character as input from the user.
# Count how many 
# times that character appears in the string using a loop.
# (Do not use any built-in functions)
#
# Example:
# Enter string: banana
# Enter character to search: a
# Output:
# 'a' appears 3 times
"""

# alpha = "banana"
# chr = "a"
# count = 0
# for ch in alpha:
#     if ch == chr:
#         count += 1
# print(count)

"""
# Q9. Check Harshad (Niven) Number
# Take an integer N as input and 
# check whether it is a Harshad Number.
# A Harshad number is a number 
# that is completely divisible by the sum of its digits.
#
# Example 1:
# Input: 18  -> Sum of digits: 1 + 8 = 9 -> 18 % 9 == 0
# Output: Harshad Number
# Example 2:
# Input: 14  -> Sum of digits: 1 + 4 = 5 -> 14 % 5 != 0
# Output: Not a Harshad Number
"""

# def is_harhd(n):
#     on = n
#     t = 0
#     while n >0:
#         ld = n%10
#         t = t +ld
#         n = n//10
#     if on%t == 0:
#         return "harshad number"
#     else:
#         return "no"

# print(is_harhd(18))
    

# Q8. Print All Numbers Ending with 7 from 1 to N
#
# Take an integer N as input and 
# print all numbers from 1 to N that end with the digit 7.
#
# Example:
# Input: 40
# Output:
# 7 17 27 37
"""
# write a function of this code and return me list
# return 
# list [] 
# append -
"""

# def rr(n):
#     l = []
#     # n = int(input("enter your number:- "))
#     for i in range(1,n+1):
#         if i %10 ==7:
#             l.append(i)
#     return l
# print(rr(40))

"""
# Q. Digit Frequency

# Take an integer N as input and count how many times
# each digit from 0 to 9 occurs in the number.
#
# Example:
# Input: 122333
#
# Output:
# 1 -> 1
# 2 -> 2
# 3 -> 3
"""

# n = int(input("enter your number:- "))
# for i in range(0,10):
#     count = 0
#     temp = n
#     while temp>0:
#         ld = temp%10
#         if ld == i:
#             count += 1
#         temp = temp//10
#     if count>0:
#         print(f"{i}  =  {count}")

# n = 11002233
# for i in range(10):
#     temp = n
#     count = 0
#     while temp > 0:
#         ld = temp%10
#         if ld == i:
#             count += 1
#         temp = temp//10
#     if count > 0:
#         print(f"{i} -> {count}")

# n = int(input())
# for i in range(10):
#     temp  =0 
#     count = 0
#     while temp>0:
#         ld = temp %10
#         if ld == i:
#             count +=1
#         temp = temp//10
#     if count>0:
#
#          print(f"{i} = {count}")

# n = int(input())
# small = 9
# while n>0:
#     ld = n%10
#     if ld <  small:
#         small = ld
#     n = n//10
# print(small)


"""
# Q. ATM Machine Simulation
#
# Write a Python program to simulate an ATM machine with the following rules:
#
# 1. PIN Verification:
#    - Default correct PIN is 1234.
#    - User gets a maximum of 3 attempts to enter the correct PIN.
#    - If entered incorrectly 3 times, print "Card Blocked! Please contact your bank." and terminate.
#
# 2. Main Menu (runs continuously until user exits):
#    - Initial Account Balance = ₹5000. 
#    - If PIN is correct, show the menu options:
#        1. Check Balance
#        2. Deposit Cash
#        3. Withdraw Cash
#        4. Exit
#
# 3. Operations:
#    - Option 1: Display the current balance.
#    - Option 2: Ask for deposit amount, add it to balance, and display updated balance.
#    - Option 3: Ask for withdrawal amount.
#                If amount <= balance, deduct and print "Withdrawal Successful".
#                Otherwise, print "Insufficient Balance!".
#    - Option 4: Print "Thank you for using our ATM. Have a nice day!" and exit the loop.
#    - Any other option: Print "Invalid Choice! Please choose 1 - 4."
"""
# main_menu = False
# attempts = 3
# for i in range(attempts):
#     pin = int(input("enter your pin:- "))
#     if pin == 1234:
#         main_menu = True
#         break
#     else:
#         attempts -= 1
#         if attempts >0:
#             print(f"wrong pin only {attempts} left")
#         else:
#             print("card blocked please contact your bank")

# balance = 5000
# # if main_menu == True:
# while main_menu :
#         print("1. check balance")
#         print("2. Deposit Cash")
#         print("3. Withdraw Cash")
#         print("4. Exit")
#         option = int(input("please choose options:- "))
#         if option == 1:
#             print(f"your current balace is {balance}")
#         elif option == 2:
#             amt = int(input("enter amount to deposit"))
#             balance = balance +amt
#             print(f"current balace is {balance}")
#         elif option == 3:
#             withdraw = int(input("enter amount to withdraw:- "))
#             if withdraw <= balance:
#                 balance = balance - withdraw
#                 print("withdrawal successful")
#             else:
#                 print("Insufficient Balance!")
#         elif option == 4:
#             print("Thank you for using our ATM. Have a nice day!")
#             break
#         else:
#             print( "Invalid Choice! Please choose 1 - 4.")
# main_menu = False
# attempts = 3
# for i in range(attempts):
#     pin = int(input("enter your pin:- "))
#     if pin == 1234:
#         main_menu  = True
#     else:
#         attempts -= 1
#         if attempts >0:
#             print(f"wrong pin only {attempts} left")
#         else:
#             print("card blocked")

# balance = 5000
# while main_menu:
#     print("1. check balance")
#     print("2. deposit amount")
#     print("3. withdraw amount")
#     print("4. Exit")
#     option = int(input("choose option: -"))
#     if option == 1:
#         print(f"your current balace is ${balance}")
#     elif option == 2:
#         dep = int(input("enter amount to deposit"))
#         balance = balance + dep
#         print(f"your updated balance is ${balance}")
#     elif option == 3:
#         wit = int(input("enter amount to withdraw"))
#         if wit <= balance:
#             balance = balance - wit
#             print("withdrawal successful")
#             print(f"your updated balance is ${balance}")
#         else:
#             print("bankrupt")
#     elif option == 4:
#         print ("Thank you for using our ATM. Have a nice day!" )
#         break
#     else:
#         print("Invalid Choice! Please choose 1 - 4.")




"""
# Find the Pair with the Given Sum
#
# Find all pairs of elements whose sum equals a given target.
#
# Example:
# Input: [2, 4, 3, 5, 7, 8]
# Target: 10
#
# Output:
# (2, 8)
# (3, 7)
"""

# arr =[2, 4, 3, 5, 7, 8]
# n = len(arr)
# target = 10
# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i] + arr[j] == target:
#             print(arr[i] , arr[j])
            

# sen = "Python.is.easY.and.python.is.powerfuL.and.Easy"
# sen = sen.lower()
# # print(sen)
# words = [] 
# # words = sen.split(" ")
# word =""

# for ch in sen:
#     if ch!=".":
#         word+=ch
#     else:
#         words.append(word)
#         word =""
# words.append(word)
# print(word)
# print(words)

# # ['python', 'is', 'easy', 'and', 'python', 'is', 'powerful', 'and' ,'easy]
# dup = []

# for i in range(len(words)):
#     count =0
#     for j in range(len(words)):
#         if words[i] == words[j]:
#             count +=1
#     if count>=2 and words[i] not in dup:
#         dup.append(words[i])
# print(dup)

sen = "Python is easy and python is powerful and easy"
# sen = sen.upper()
# print(sen)

# words = []
# word = ""
# for ch in sen:
#     if ch !=  " ":
#         word += ch
#     else:
#         words.append(word)
#         word = ""
# words.append(word)
# print(words)

# ans = []
# for i in range(len(words)):
#     count = 0
#     for j in range(len(words)):
#         if words[i] == words[j]:
#             count += 1
#     if count>1 and words[i] not in ans:
#         ans.append(words[i])
# print(ans)

# sen = "Python is easy and python is powerful and easy"
# sen = sen.lower()
# words = []
# words = sen.split(" ")

# ans = []
# for i in range(len(words)):
#     count = 1
#     for j in range(i+1,len(words)):
#         if words[i] == words[j]:
#             count += 1
#     if count >1:
#         ans.append(words[i])
# print(ans)

# arr = [10, 20, 30, 40, 50]
# m = len(arr)
# sub = [20, 30, 40]
# n = len(sub)

# for i in range(m-n+1):
#     if arr[i:i+n] == sub:
#         print("sublist found")
#         break
# else:
#     print("sublist not found")

# arr = [1,2,3,4,5]
# k = 2
# k = k%(len(arr))
# for i in range(k):
#     last = arr.pop()
#     arr.insert(0,last)
# print(arr)



# arr = [1,2,3,4,5]
# k = 2
# k = k%(len(arr))

# for i in range(k):
#     l = arr.pop()
#     arr.insert(0,l)
# print(arr)


# arr = [1,2,3,4,5]
# k = 2
# k = k%(len(arr))
# for i in range(k):
#     l = arr.pop()
#     arr.insert(0,l)
# print(arr)


# arr = [1,2,3,4,5]
# k = 2
# k = k%(len(arr))
# for i in range(k):
#     last = arr.pop()
#     arr.insert(0,last)
# print(arr)


# arr = [1,2,3,4,5]
# k = 2
# k = k%(len(arr))
# for i in range(k):
#     last = arr.pop()
#     arr.insert(0,last)
# print(arr)

# arr1 = [1, 4, 7, 10]
# arr2 = [2, 3, 8, 9]
# n1 = len(arr1)
# n2 = len(arr2)
# l2 = []
# i = 0
# j = 0

# while i < n1 and j<n2:
#     if arr1[i] < arr2[j]:
#         l2.append(arr1[i])
#         i += 1
#     else:
#         l2.append(arr2[j])
#         j += 1
# while i < n1:
#     l2.append(arr1[i])
#     i += 1
# while j < n2:
#     l2.append(arr2[j])
#     j += 1

# print(l2)

# sen = "Eat sleep code and repeat code and eat clean"
# sen = sen.lower()
# words = sen.split(" ")
# d = {}
# for word in words:
#     l = len(word)
#     l2 = []
#     for word1 in words:
#         if len(word1) == l and word1 not in l2:
#             l2.append(word1)
#     d[l] = l2
# print(d)

#  create an another list and store the reverse value

# l2 = []
# for i in range(len(l)-1,-1,-1):
#     l2 = l[i]
#     print(l2)


# l = [10,20,30,40,50,60,70,80]
# l2 = []
# for i in range(len(l) - 1,-1,-1):
#     l2.append(l[i])
# print(l2)

# arr = [10, 20, 30, 40, 50]
# l = []
# for i in range(len(arr)-1,-1,-1):
#     l.append(arr[i])
# print(l)

# arr = [10, 20, 30, 40, 50]
# n = len(arr)
# mid = n//2
# for i in range(mid):
#     arr[i] , arr[n-i-1] = arr[n-i-1] , arr[i]
# print(arr) 

# arr = [10, -5, 20, -3, 0, 8]
# l_even = []
# l_odd = []
# for i in range(len(arr)):
#     if arr[i] > 0:
#         l_even.append(arr[i])
#     elif arr[i] < 0:
#         l_odd.append(arr[i])
# print(l_even)
# print(l_odd)

# arr  =[10, 20, 30, 40]
# total = 0
# for i in arr:
#     total += i
# print(total/len(arr))

# Input: [2, 96, 69, 77, 145, 20]
# Output: Max element = 145 
# found at 4 index


# arr  = [2, 96, 69, 77, 145, 20]
# index = 0
# large = arr[0]
# for i in range(len(arr)):
#     if arr[i] > large:
#         large = arr[i]
#         index = i
# print(f"Max element = {large}")
# print(f"found at {index} index")

# arr  =[1, 2, 4, 5]
# n = len(arr)
# og_n = n+1
# og_sum = ((og_n) * (og_n+1))//2
# real_sum = 0
# for i in range(n):
#     real_sum += arr[i]
# misiing = og_sum - real_sum
# print(misiing)


# arr  =[10, 20, 30, 40, 50]
# flag = True
# for i in range(len(arr)-1):
#     if arr[i] > arr[i+1]:
#         flag = False
#         break
# if flag == True:
#     print("list is sorted")
# else:
#     print("list is not sorted")

# arr  =[10, 20, 30, 40, 50]
# count = 0
# for i in range(1,len(arr)):
#     if arr[i] > arr[i-1]:
#         count += 1
        
# if count == len(arr) - 1 :
#     print("list is sorted")
# else:
#     print("list is not sorted")

# arr  = [2, 3, 15, 15, 3, 2]
# flag = True
# n =len(arr)
# for i in range(n//2):
#     if arr[i] != arr[n-i-1]:
#         flag = False
#         break
# if flag == True:
#     print("palindromic list")
# else:
#     print("not")

# arr1 = [1, 4, 7, 10]
# arr2 = [2, 3, 8, 9]
# l = []

# n1 = len(arr1)
# n2 = len(arr2)
# i = 0 
# j = 0
# while i < n1 and j < n2:
#     if arr1[i] < arr2[j]:
#         l.append(arr1[i])
#         i += 1
#     else:
#         l.append(arr2[j])
#         j += 1
# while i < n1:
#     l.append((arr1[i]))
#     i += 1
# while j < n2:
#     l.append(arr2[j])
#     j += 1
# print(l)

# arr = [1,2,3,4,5]
# k = 2
# k = k%len(arr)
# for i in range(k):
#     last = arr.pop()
#     arr.insert(0,last)
# print(arr)
# sen = "Python is easy and python is powerful and easy"
# sen = sen.lower()
# # words = []
# words = sen.split(" ")
# # print(words)


# ans = []
# for i in range(len(words)):
#     count = 0
#     for j in range(i+1,len(words)):
#         if words[i] == words[j]:
#             count += 1
#     if count > 1:
#         ans.append(words[i])
# print(ans)


# d = {"ravi" : 80, "Rohan" : 23, "Devraj" : 88}
# d.pop("Rohan")
# print(d)

# d = {"Ravi": 70,"abhishek":33,"rohan" : 12}
# total = 0
# for i in d.values():
#     total += i
# print(total)

"""**Q1. Create a Dictionary**

Create a dictionary containing your name, age, 
and city. Print the dictionary.

**Example Output:**

{'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
"""
# d = {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
# print(d)

# d = {'name': 'Rahul', 'age': 20}
# d['course'] = 'python'
# print(d)


# d  = {'a': 10, 'b': 15, 'c': 20, 'd': 7}
# count_evn = 0
# count_odd = 0
# for i in d:
#     if d[i] %2==0:
#         count_evn +=1
#     else:
#         count_odd += 1
# print(count_evn)
# print(count_odd)

# d =  {'a': 10, 'b': 20, 'c': 30}
# target = 20
# for i in d:
#     if d[i] == target:
#         print(i)
#         break


# d = {"1":10,"2":20,"3":30,"4":40}
# print(d.get("5"))


# n = int(input("tell your number:- "))
# for i in range(n,n*10+1,n):
#     print(i)
""
"""# n = int(input("enter your number:- "))
# t = 1
# for i in range(1,n+1,1):
#     t *= i
# print(t)"""""

# num = int(input("tell your number:- "))

# for i in range(1,num+1):
#     if num%i==0:
#         count = 0
#         for j in range(1,i+1):
#             if i%j == 0:
#                 count += 1
#         if count == 2:
#             print(i)

# num = int(input("tell your number:- "))
# count = 0
# for i in range(1,num+1):
#     if num%i == 0:
#         count += 1
# if count == 2:
#     print("prime")
# else:
#     print("not")

# name = "AbhiSHEK"
# count_up = 0
# count_l = 0
# for i in name:
#     if i.isupper():
#         count_up += 1
#     elif i.islower():
#         count_l +=1 
# print(count_up,count_l)

# s = 0
# while(n!=0):
#     ld = n%10
#     s = s*10+ld
#     n= n//10
# print(s)

# n = int(input("enter num:- "))
# on = n
# t = 0
# l = len(str(n))
# while n >0:
#     ld = n%10
#     t = t + (ld**l)
#     n = n//10 

# if on == t:
#     print("armstrong")
# else:
#     print("not")

'''**Q3. Monthly Savings Analysis**

A person records the amount saved on **7 different days**.

Write a program to calculate the **total savings** and 
determine how many days the savings were **greater than ₹500**.
'''

# sum_save = 0
# count = 0
# for i in range(8):
#     save = int(input("enter:- "))
#     sum_save += save
#     if save > 500:
#         count += 1
# print(sum_save)
# print(count)
    

'''Take N numbers as input and determine the largest number among them.

Example:
Input:
5
10                                # very very imp q can be done without arrays think!!!!!
25
7
18
12

Output:
25
'''

# n = int(input("enter"))
# large = 0
# for i in range(n):
#     num = int(input("enter numbers:- "))
#     if num>large:
#         large = num 
# print(large)

# n = int(input("enter: "))
# on = n
# t = 0
# for i in range(1,n):
#     if n%i==0:
#         t += i
# if t == on:
#     print("perfect")
# else:
#     print("not")

"""Q2. Difference Between Largest and Smallest
+Take N numbers as input and calculate the difference between the largest and smallest number.
Example:
Input:
5
10
25            
7
18
12
Output:
22
"""

# n = int(input("enter num "))
# large = float('-inf')
# small = float('inf')

# for i in range(n):
#     nums = int(input("enter:- "))
#     if nums >large:
#         large = nums

#     if nums < small:
#         small = nums
# print(large)
# print(small)
# print(large - small)

# n = 5832
# large = float('-inf')
# sl = float('-inf')
# while n>0:
#     ld = n%10
#     if ld > large:
#         sl = large
#         large = ld
#     elif ld > sl and ld!= large:
#         sl = ld
#     n = n//10
# print(sl)
# print(large)
    
# l = [10,20,30,40,50,60,70,80]
# l2 = []
# for i in range(len(l)-1,-1,-1):
#     l2.append(l[i])
# print(l2)

# ar = [10, -5, 20, -3, 0, 8]
# l_evn =[]
# l_odd =[]
# for i in ar:
#     if  i >0:
#         l_evn.append(i)
#         # print(i , end= "")
#     elif i <0:
#         l_odd.append(i)
# print(l_evn)
# print(l_odd)

# arr = [2, 96, 69, 77, 145, 20]
# large = float("-inf")
# index = 0
# for i in range(len(arr)):
#     if arr[i] > large:
#         large = arr[i]
#         index = i

# print(large)
# print(index)

"""
# Find the Missing Number
#
# A list contains numbers from 1 to N, but one number
# is missing. Write a program to find the missing number.
#
# Example:
# Input: [1, 2, 4, 5]
#
# Output:
# Missing Number = 3
"""

# arrr = [1, 2, 4, 5]
# n = len(arrr)
# og_n = n+1
# real_sum = 0
# og_sum = ((og_n)*(og_n+1))//2
# for i in arrr:
#     real_sum += i
# print(og_sum - real_sum)


# l = [10, 20, 30, 40, 50]
# for i in range(len(l)-1):
#     if l[i] > l[i+1]:
#         print("list is not sorted")
#         break
# else:
#     print("sorted") 

# arr = [2, 3, 15, 15, 3, 2]
# is_palin = True
# n = len(arr)
# for i in range(n//2):
#     if arr[i] != arr[n-i-1]:
#         is_palin = False
#         break
# if is_palin:
#     print("palindromic")
# else:
#     print("not")

# arr = [1, 2, 3, 4, 5, 6]
# evn = []
# odd = []
# for i in arr:
#     if i%2==0:
#         evn.append(i)
#     else:
#         odd.append(i)
# print(evn)
# print(odd)

# arr =  [1, 2, 3, 2, 4, 1, 5]
# arr2 = set(arr)

# print(list(arr2))

# d  = d = {'a': 10, 'b': 25, 'c': 5, 'd': 40}

# small = d['a']
# for i in d:
#     if d[i] < small:
#         small = d[i]

# print(small)

"""
# Q3. Check Strong Number 
#
# Take an integer N as input and
# check whether it is a Strong Number.
# A Strong Number is a number
# whose sum of factorials of its
# digits equals the original number.
#
# Example:
# Input: 145
# 1! = 1
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# Sum: 1 + 24 + 120 = 145
# Output: Strong Number
"""
# n = int(input("enter"))
# on = n
# total = 0
# while n >0:
#     fact = 1
#     ld = n%10
#     for i in range(1,ld+1):
#         fact *= i
#     total += fact
#     n = n//10
    
# if total == on:
#     print("strong num")
# else:
#     print("not")

# n = int(input("enter the number "))
# a = 0 
# b = 1
# for i in range(n):
#     print(a,end= "")
#     c = a+b
#     a =b
#     b = c

# n =  122333

# for i in range(1,11):
#     count = 0
#     temp = n
#     while temp >0:
#         ld = temp%10
#         if ld == i:
#             count +=1
#         temp = temp//10
#     if count>0:
#         print(f"{i} -> {count}")
    

# arr = [10, 20, 30, 40, 50]
# sub = [20, 30, 40]
# n = len(arr)
# m = len(sub)

# for i in range(n-m+1):
#     if arr[i:i+m] == sub:
#         print("found")
#         break
# else:
#     print("not")

# arr1 = [1, 4, 7, 10]
# arr2 = [2, 3, 8, 9]

# n1 = len(arr1)
# n2 = len(arr2)
# l2 = []
# i = 0
# j = 0

# while i<n1 and j<n2:
#     if arr1[i] < arr2[j]:
#         l2.append(arr1[i])
#         i +=1
#     else:
#         l2.append(arr2[j])
#         j += 1

# while i <n1:
#     l2.append(arr1[i])
#     i += 1
# while j<n2:
#     l2.append(arr2[j])
#     j += 1

# print(l2)


# arr = [1,2,3,4,5]
# k = 2
# k = k%(len(arr))

# for i in range(k):
#     last  =arr.pop()
#     arr.insert(0,last)

# print(arr)

# sen = "Python is easy and python is powerful and easy"
# sen  =sen.lower()

# words = []
# words = sen.split(" ")
# ans = []

# for i in range(len(words)):
#     count = 1
#     for j in range(i+1,len(words)):
#         if words[i] == words[j]:
#             count += 1
#     if count >=2 and words[i] not in ans:
#         ans.append(words[i])
# print(ans)


# sen = "Eat sleep code and repeat code and eat clean"

# sen = sen.lower()
# l = len(sen)
# words = []
# ans = {}
# words = sen.split(" ")
# for ch in words:
#     l = len(ch)
#     temp = []
#     for ch2 in words:
#         if len(ch2) == l and ch2 not in ans:
#             temp.append(ch2)
#     ans[l] = temp
# print(ans)
n = 10
count = 0
while n >0:
    print(n)
    count += 1
    n = n - 3
print(f"Total execution: {count}" )