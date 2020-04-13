# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
x = input().split()
n = int(x[1])
perm = sorted(list(permutations(x[0],n)))
for n in range(0,len(perm)):
    print("".join(perm[n]))