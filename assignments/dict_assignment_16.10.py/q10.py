"""Q10.Count Positive and Negative Values
Given a dictionary containing numbers, count how 
many values are positive and
how many are negative.

Example:
Input: {'a': 10, 'b': -5, 'c': 20, 'd': -8, 'e': 7}

Output:
Positive: 3
Negative: 2
"""

d = {'a': 10, 'b': -5, 'c': 20, 'd': -8, 'e': 7}
positive = 0
negative = 0
for i in d.values() :
    if i >0:
        positive += 1
    elif i<0:
        negative += 1
print(f"positive: {positive}")
print(f"negative: {negative}")