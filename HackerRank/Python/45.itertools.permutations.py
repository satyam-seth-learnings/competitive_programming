# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
k=input().split()
for i in list(permutations(sorted(k[0]),int(k[1]))):
    print("".join(i))
