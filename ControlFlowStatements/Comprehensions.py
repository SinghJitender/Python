# comprehensions
# Lets se we need to convert a string into a list for each letter
# Way one - using loop

word = "Python"
mylist1 = []
for letter in word:
    mylist1.append(letter)
print(mylist1)

# Second Way - Using comprehensions
mylist2 = [letter for letter in word]
print(mylist2)

# other uses - Get a list with every number in range's square root
mylist3 = [num**2 for num in range(0,10)]
print(mylist3)

# complex uses - using if statement along this
mylist4 = [num for num in range(0,20) if(num%2==0)]
print(mylist4)
# else can also be used but the order changes - Example
mylist5 = [x if x%2 == 0 else 'ODD' for x in range(0,10)]
print(mylist5)

# nested loop in list comprehensions
mylist6 = [x*y for x in [2,4,6] for y in [1,10,100]]
print(mylist6)
