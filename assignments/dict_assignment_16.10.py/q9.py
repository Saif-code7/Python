"""Q9.Count Values Equal to a Given Number
Given a dictionary and a number, count how many 
times that number appears as a value
in the dictionary.

Example:
Input: {'a': 10, 'b': 20, 'c': 10, 'd': 30}
Number: 10
Output: 2
"""

d = {'a': 10, 'b': 20, 'c': 10, 'd': 30}
Number = int(input("enter your number:- "))
count = 0
for i in d.values():
    if i == Number:
        count += 1
print(count)