# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
ordinary_dictionary = OrderedDict()
for _ in range(0,n):
    item = input()
    if ordinary_dictionary.get(item) != None :
        ordinary_dictionary[item] = ordinary_dictionary.get(item) + 1
    else :
        ordinary_dictionary[item] = 1
print(len(ordinary_dictionary.keys()))
print(*ordinary_dictionary.values())