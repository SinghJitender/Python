# Assigning function to a variable
def hello():
    print("Printing Hello()")

x = hello
x()

# Internal Functions (Function inside function)
# They can only be invoked inside the original/parent function

def func1():
    print("Inside function 1")
    def func2():
        print("Inside function 2")
    def func3():
        print("Inside function 3")
    print("End of function 1")

func1()