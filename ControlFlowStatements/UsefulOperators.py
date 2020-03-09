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