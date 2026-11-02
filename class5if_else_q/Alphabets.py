"""
Question 1: Vowel or Consonant

Write a Python program that accepts an English alphabet
from the user and checks
whether it is a vowel or a consonant.

Example:
Enter a character: e

Output: Vowel
"""


alpha = input("enter an english alphabet :- ")
# if alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u':
#     print ("vowel")
# else:
#     print("consonant")

if alpha in "aeiouAEIOU":   # in tab use karte hai jab baar baar or use naa krna pade 
    print("vowel")           # internall start to end har jagah check krta h just like loops
else:
    print("consonent")

