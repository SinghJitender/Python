# Tuples are very similar to lists but they are immutable. i.e once a value is assigned it cannot be changed.
# Tuples are defined in brackets " (  ) "

tup = (1,2,3,4,5)
print(tup)

# tuples can also contains any type of element
tup2 = ("One",2,3.00)
print(tup2)

# tuples cannot be reassigned with any value like in list
# Example - tup2[0] = "1" will give an error

# tuples have 2 methods - count and index
print(tup2.count('One')) # count total occurences of given element in tuple
print(tup2.index('One')) # return index of first occurence of given element in tuple

# as in the case of strings, we can use indexing and slicing in tuples as well
print(tup[1:])
print(tup[0])
print(tup[-1])
