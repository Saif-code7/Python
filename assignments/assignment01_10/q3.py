'''Q3.

Take N numbers as input. Calculate their average.

Example:
Input:
5
10
20
30
40
50
Output:
30.0
'''

N = int(input("enter your number:- "))
sum = 0
for i in range(1,N+1):
    n = int(input("tell number:- "))
    sum += n
print(sum/N)
