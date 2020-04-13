# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
x = input().split()
n = int(x[1])
for i in range(1,n+1):
    comb = list(combinations(sorted(x[0]),i))
    for m in range(0,len(comb)):
        print("".join(comb[m]))
