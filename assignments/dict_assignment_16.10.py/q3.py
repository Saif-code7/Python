"""Q3 . Count Even and Odd Values
Count how many values in a dictionary are 
even and how many are odd.
Example:
Input: {'a': 10, 'b': 15, 'c': 20, 'd': 7}

Output:
Even: 2
Odd: 2
"""

d = {'a': 10, 'b': 15, 'c': 20, 'd': 7}
count_evn =0
count_odd = 0
for keyy,elem in d.items():
    if elem %2 ==0:
        count_evn += 1
    else:
        count_odd += 1
print(f"Even: {count_evn}")
print(f"Odd: {count_odd}")


d = {'a': 10, 'b': 15, 'c': 20, 'd': 7}
count_evn =0
count_odd = 0
for elem in d.values():
    if elem %2 ==0:
        count_evn += 1
    else:
        count_odd += 1
print(f"Even: {count_evn}")
print(f"Odd: {count_odd}")