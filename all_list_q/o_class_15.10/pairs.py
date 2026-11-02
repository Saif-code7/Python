
"""
# Find the Pair with the Given Sum
#
# Find all pairs of elements whose sum equals a given target.
#
# Example:
# Input: [2, 4, 3, 5, 7, 8]
# Target: 10
#
# Output:
# (2, 8)
# (3, 7)
"""


arr = [2, 4, 3, 5, 7, 8]
target = 10
n = len(arr)
for i in range(n):
    for j in range(i+1,n):
        if (arr[i] + arr[j]) == target:
            print(f"({arr[i]},{arr[j]})")

"""iss q me bas hume pair bana k check krna hai kee sum 10 toh nhi agr hai 
toh print it for this we need two loop outer one for the primary element for 
first iteration its 2 then 4 and so on and inner loop is for the remaining next elemet 
like (2,4) (2,3) islia wo loop i+1 se start hoga aise kr kr ke toh inner loop 4 ,3 ye sab 
ko access krne k lia hai 
"""