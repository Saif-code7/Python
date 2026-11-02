"""Q8. Count Even and Odd Digits
Create a function count_even_odd() that takes a number 
and returns the count of even and odd digits.

Example:
Input: 123456
Output:
Even digits: 3
Odd digits: 3
"""
def count_even_odd(n):
    count_evn = 0
    count_odd = 0
    while n>0:
        ld = n%10
        if ld%2 == 0:
            count_evn += 1
        else:
            count_odd += 1
        n = n//10
    return count_evn , count_odd

num = int(input("enter a number:- "))

print(count_even_odd(num))



# even, odd = count_even_odd(num)

# print("Even digits:", even)
# print("Odd digits:", odd)

# tuple