# map() and filter()
# lambda expression are anonymous functions
def sqrt(num):
    return num**2
mylist = [1,2,3,4,5]
print(list(map(sqrt,mylist)))