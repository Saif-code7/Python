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

# alpha = input("enter string: -")
# count = 0


# for ch in alpha:
#     if ch in "AEIOUaeiou":
#         count += 1
# print(count)



# txt = input("enter your text")
# count = 0
# for ch in txt:
#     if ch in "aeiouAEIOU":
#         count += 1
# print(count)


text = input("enter your text:- ")
count =0
for ch in text:
    if ch in "aeiouAEIOU":
        count += 1
print(count)

txt = input("enter:- ")

count =0
for ch in txt:
    if ch in "aeiouAEIOU":
        count += 1
print(count)
