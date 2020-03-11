# map() and filter()
# lambda expression are anonymous functions

# map() is used to map each item in the list to the given function and returns a list
def sqrt(num):
    return num**2
mylist = [1,2,3,4,5]
print(list(map(sqrt,mylist)))

#filter() can be used to filter the list based upon a condition
def check_len(str):
     return len(str)%2==0
list_names=["Jitender","Jitu","Jagii","Amit"]
print(list(filter(check_len,list_names)))

# Converting normal methods into lambda expression
# def function_name(parameter):
#    return expression
# To lambda expression
# lambda parameter: expression

var  = lambda str: len(str)%2==0
print(var("ABC"))

print(list(filter(lambda str:str[0].lower() in "aeiou", list_names)))

