# Funtions can be used as a placeholder for a code which will be used multiple times
# Functions are declared in following way
# def function_name(parameters):
#   body of function

# Functions can be of two types - Returning funtion and Non returning function

# Non Returning functions - Does not return anything

def print_name(name):
    print("Hello "+name)

print_name("Jitender")

# Parameters in a funtion can be assigned a default value.
def default_value(value = 10):
    print(value)

default_value() # Since no value is provided. default value will be printed
default_value(20)

# functions can also be provided with documentation elcosed in ''' .... '''

def documentation():
    '''
    This is a demonstration to show 'How to add function documentation'
    Here we can write about inputs, output and functioning or usage of the function like :
    :return: nothing
    '''
    print("You can type help(funtion_name) to read the documentation i.e. help(documentation) ")

help(documentation)

# 'return' keyword can be used to return a value from a function

def add(a=0,b=0):
    return a+b

sum = add(10,20)
print(sum)


def pig_latin(word):
    if word[0] in "aeiou":
        result = word+"ay"
    else:
        result = word[1:]+word[0]+"ay"
    return result

print(pig_latin("apple"))
print(pig_latin("word"))

# To make a function takes in multiple agruments/parameters we can use '*args' or '*kwargs'
# *args - stands for positional arguments. This is accepted as a tuple. we can use any name like '*name' for this.
# *kwargs - stands for keyword arguments. This is accepted as a dictionary. we can use any name here as well.
# Both of them can also be used together provided we pass the arugment in specific order.

def sumAll(*args):
    import builtins
    print(builtins.sum(args))

def keyValue(**kwargs):
    print(kwargs)
    print(kwargs["name"])

sumAll(10,20,30,40,50)
keyValue(name="Jitender", age=24)
