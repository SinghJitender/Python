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

# Python provides alot of inbuilt methods such as sort(), reverse(), pop(), append()
list.sort()
print(list) # prints sorted list. sort() method do not return anything, it sorts the original list
list.reverse()
print(list)
list.append(9) # adds element to the end of list
print(list)
item1 = list.pop() # removes last element
item2 = list.pop(0) # remove element with the index provided. By default its -1;
print(f"{item1} and {item2}")
print(list)

x = None # Null as in Java

# Dictionaries are just like Hashtables
dictionary = {'key1':100, 'key2':200, 'key3':300}
print(dictionary)
print(dictionary['key2']) # prints value of key 2;

dictionary = {'key1':130.30, 'key2':[10,20,30], "key3":{'insideKey':200}}
print(dictionary)
print(dictionary['key2'])
print(dictionary['key3']['insideKey'])

dictionary['key4'] = 6969.69 # adding new key to dictionary
print(dictionary)

print(dictionary.values())
print(dictionary.keys())
