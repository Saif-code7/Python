"""Q5. Find a Key with a Given Value
Given a dictionary and a value, find the key 
associated with that value.

Example:
Input: {'a': 10, 'b': 20, 'c': 30}
Value: 20
Output: b
"""

d = {'a': 10, 'b': 20, 'c': 30}
Value = int(input("enter your vakue:- "))

for i,j in d.items():
    if j == Value:
        print(i)
        break
else:
    print("not found")