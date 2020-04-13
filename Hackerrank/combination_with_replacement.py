# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
x = input().split()
n = int(x[1])
comb = list(combinations_with_replacement(sorted(x[0]),n))
for m in range(0,len(comb)):
    print("".join(comb[m]))
