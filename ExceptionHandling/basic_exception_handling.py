'''
 Exception handling can be used to handle errors.
 There are various variations in which exception handling can be used in python
 try:
   try-block-code
 except:
   except-block-code
 else:
   else-block-code

 if try block is executed successfully. Then the control goes to else block.
 If not then except block is executed but not else block
 else block is not necessary. try-expect will also work
'''


def divide(arugment_one, argument_two):
    '''
    :param arugment_one: Argument Type 1 - Integer
    :param argument_two: Argument Type 2 - Integer
    :return: Argument 1 divide by Argument 2
    '''
    return arugment_one / argument_two


# Example 1
try:
    RESULT = divide(0, 1)
    print("Result is {}".format(RESULT))
except ZeroDivisionError:
    print("Exception Occured : ")
else:
    print("This is else block")

# Exammple 2
try:
    RESULT = divide(1, 0)
    print("Result is {}".format(RESULT))
except ZeroDivisionError:
    print("Exception Occured : ")
else:
    print("This is else block")

# Example 3
try:
    RESULT = divide(2, 4)
    print("Result is {}".format(RESULT))
except ZeroDivisionError:
    print("Error Occured.")

# If something else needs to be executed after the except block then 'finally block should be used.

# Example 4 - Exception not thrown
try:
    RESULT = divide(0, 1)
    print("Result is {}".format(RESULT))
except ZeroDivisionError:
    print("Exception Occured : ")
finally:
    print("This is finally block. It will be executed no matter what")

# Example 5 - Exception thrown
try:
    RESULT = divide(4, 0)
    print("Result is {}".format(RESULT))
except ZeroDivisionError:
    print("Exception Occurred: ")
finally:
    print("This is finally block. It will be executed no matter what")

# Example 6 - Finally with else-block
try:
    RESULT = divide(4, 8)
    print("Result is {}".format(RESULT))
except ZeroDivisionError:
    print("Exception Occurred : ")
else:
    print("This is else block")
finally:
    print("This is finally block. It will be executed no matter what")
