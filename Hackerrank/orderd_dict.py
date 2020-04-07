 # Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
ordinary_dictionary = OrderedDict()
n = int(input())
for i in range(0,n):
    item = input().split()
    if ordinary_dictionary.get(' '.join(item[0:len(item)-1])) != None:
        ordinary_dictionary[' '.join(item[0:len(item)-1])] = ordinary_dictionary.get(' '.join(item[0:len(item)-1]))+ int(item[len(item)-1])
    else :
        ordinary_dictionary[' '.join(item[0:len(item)-1])] = int(item[len(item)-1])
for items in ordinary_dictionary:
    print(f'{items} {ordinary_dictionary.get(items)}')
