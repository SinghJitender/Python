# range(start,end,step)
# range function can be used to generate number with a specific range

for num in range(0,10,1):
    print(num)

mylist = list(range(0,20,2)) # create a list including numbers uptill 19 with stepsize 2.
print(mylist)

# enumerate() can be used to create a tuple for index and value
word ="abcdef"

for item in enumerate(word):
    print(item)

for index,item in enumerate(word):
    print(f"{index} : {item}")

# zip() zips together two lists and returns a tuple. Every item is zipped to other items in other list at corresponding index
list1 = [1,2,3]
list2= ["a","b","c","d"]
result = zip(list1,list2)
for item in result:
    print(item)

# to get the zip() output as a list
list3 = list(zip(list1,list2))
print(list3)

# in operator can be used to check if items is there in a list - returns a  boolean

print('a' in ' word')
print(1 in [2,3,4,5,1])
print(345 in {'mkey':345}.keys())
print(345 in {'mkey':345}.values())



