"""Q8. Create a Dictionary from Two Lists
Given two lists, create a dictionary where the 
first list contains keys and the second list
contains values.

Example:
Keys: ['a', 'b', 'c']
Values: [10, 20, 30]
"""

Keys = ['a', 'b', 'c']
Values = [10, 20, 30]

d = {}

for keys , value in zip(Keys , Values):
    d[keys] = value
print(d)
