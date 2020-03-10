# map() and filter()
# lambda expression are anonymous functions

# map() is used to map each item in the list to the given function and returns a list
def sqrt(num):
    return num**2
mylist = [1,2,3,4,5]
print(list(map(sqrt,mylist)))