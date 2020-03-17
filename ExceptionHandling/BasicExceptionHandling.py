# Exception handling can be used to handle errors.
# There are various variations in which exception handling can be used in python
# try:
#   try-block-code
# except:
#   except-block-code
# else:
#   else-block-code

# if try block is executed successfully. Then the control goes to else block. If not then except block is executed but not else block

def divide(a,b):
    return a/b

# Example 1
try:
    result = divide(0,1)
    print("Result is {}".format(result))
except:
    print("Exception Occured : ")
else:
    print("This is else block")

# Exammple 2
try:
    result = divide(1,0)
    print("Result is {}".format(result))
except:
    print("Exception Occured : ")
else:
    print("This is else block")