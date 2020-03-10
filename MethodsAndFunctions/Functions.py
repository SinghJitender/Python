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