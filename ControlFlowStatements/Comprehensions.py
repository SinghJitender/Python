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