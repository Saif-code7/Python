"""**Q5. Delete a Key**

Remove the key "city" from the dictionary.

**Example:**

- Input: {'name': 'Rahul', 'age': 20, 'city': 'Bhopal'}
- Output: {'name': 'Rahul', 'age': 20}
"""

d = {'name' : 'Rahul', 'age' : 20, 'city' : 'Bhopal'}
del d['city']   
print(d)