# list are similar to arrays in python. they can hold any type of data and supports indexing and slicing function juts as string

list = [1,2,3,4,5]
print(list)
list = ["one","two",'three']
print(list)
list = ["One",120,133.45]
print(list)
list = [1,2,3,4,5]
print(list[0]) # items at index - 0
print(list[1:]) # All items starting from index 1
print(len(list)) # length of list
list += [6,7,8] # adding elements/ concatenating list to another list
print(list)