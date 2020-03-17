# Exception handling can be used to handle errors.
# There are various variations in which exception handling can be used in python
# try:
#   try-block-code
# except:
#   except-block-code
# else:
#   else-block-code

# if try block is executed successfully. Then the control goes to else block. If not then except block is executed but not else block
# else block is not necessary. try-expect will also work

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

# Example 3
try:
    result = divide(2/4)
    print("Result is {}".format(result))
except:
    print("Error Occured.")

# If something else needs to be executed after the except block then 'finally block should be used.

# Example 4 - Exception not thrown
try:
    result = divide(0,1)
    print("Result is {}".format(result))
except:
    print("Exception Occured : ")
finally:
    print("This is finally block. It will be executed no matter what")