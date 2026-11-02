
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


# alpha = input("enter a text:- ")

# target = input("enter character:- ")
# count = 0

# for ch in alpha:
#     if ch == target:
#         count += 1

# print(f"{target} appears {count} times")




text = input("enter your string: -")
target = input("enter character:- ")
count = 0
for ch in text:
    if ch == target:
        count +=1
print(count)

stri = input("enter string- ")
tar = input("enter character:- ")
count = 0

for ch in stri:
    if ch == target:
        count += 1
print(count)