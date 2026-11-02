"""
Question: Group Words of a Sentence by Their Length
Given a sentence, group all unique words by their length into a
dictionary. Ignore uppercase and lowercase differences.
Example:
Input:  "Eat sleep code and repeat code and eat clean"
Output: {3: ['eat', 'and'], 5: ['sleep', 'clean'], 4: ['code'], 6: ['repeat']}
"""

sen = "Eat sleep code and repeat code and eat clean"
sen = sen.lower()
words = sen.split(" ")
ans = {}
# print(sen)
for ch in words:
    l = len(ch)
    temp = []
    for ch2 in words:
        if len(ch2) == l and ch2 not in temp:
            temp.append(ch2)
    ans[l] = temp
print(ans)
    