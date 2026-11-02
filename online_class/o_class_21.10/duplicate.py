"""
Question: Find Duplicate Words in a Sentence
Find all words that appear more than once.
Ignore uppercase and lowercase differences.
Input:
"Python is easy and python is powerful and easy"
Output:
['python', 'is', 'easy', 'and']
"""
 # my approach
sen = "Python is easy and python is powerful and easy"
sen = sen.lower()
words = []
word = ""
for ch in sen:
    if ch != " ":
        word += ch
    else:
        words.append(word)
        word = ""
words.append(word)

ans = []
for i in range(len(words)):
    count = 1
    for j in range(i+1,len(words)):
        if words[i] == words[j]:
            count += 1
    if count > 1:
        ans.append(words[i])
print(ans)
"""
sen = "Python is easy and python is powerful and easy"
sen = sen.lower()
words = []
words = sen.split(" ")
# words.append(word)   
print(words)

ans = []
for i in range(len(words)):
    count = 1
    for j in range(i+1,len(words)):
        if words[i] == words[j]:
            count += 1
    if count > 1:
        ans.append(words[i])
print(ans)"""

# sir approach
sen = "Python is easy and python is powerful and easy"
sen = sen.lower()
words = []
words = sen.split(" ")

ans = []
for i in range(len(words)):
    count = 0
    for j in range(len(words)):
        if words[i] == words[j]:
            count += 1
    if count >= 2 and words[i] not in ans:
        ans.append(words[i])
print(ans)


'''iss q me bas itna yaad rkhna kee sen ko lowercase yaa upper me bdl 
do pura phir usko list me dalne kee koshish kro using split ya or
tumhare method se phir do approach lagao 1st using sum pair done on 
o_class_15 ko yaa sir wale method se'''