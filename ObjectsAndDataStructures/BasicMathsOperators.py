# / : divide Operator
# + : addition
# - : subtraction
# * : multiply
# ** : power (a ** b - a to the power of b)
# % : modulus

print(1+2)
print(2-1)
print(2*3)
print(4/2)
print(2**3)
print(5%2)

# type(variable_name) can be used to check the type of variable
# we can assign any value to a variable in python

a = 10;
print(type(a))
a = "String"
print(type(a))
a = 100.9
print(type(a))

# float precision using .format()
value = 100/76
print(value)

print("Value = {}".format(value))
print("Value = {v:1.3f}".format(v = value)) # setting precision to 3 decimal points and width = 1. Width is nothing but the whitespace before the value in printed

