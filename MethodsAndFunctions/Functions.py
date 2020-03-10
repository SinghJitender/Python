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