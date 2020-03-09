# For iterating over the elements

list =[1,2,3,4,5,6,7,8,9,10]
for num in list:
    print(num)

str = "This is a string"
for letter in str:
    print(letter,end='_')

# tuple unpacking
list =[(1,2),(3,4),(5,6),(7,8)]
for tuple in list:
    print(tuple)
for a,b in list:
    print(a)
    print(b)