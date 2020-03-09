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

d={'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)
for item in d.items():
    print(item)
for key,value in d.items():
    print(f"{key}:{value}")
