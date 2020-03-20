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

def func4(value = 1):
    print("Inside function 4")
    def func5():
        return "Inside function 5"
    def func6():
        return "Inside function 6"
    print("End of function 4")
    if value == 1:
        return func5()
    else:
        return func6()

test = func4

print(f"Result : {test()}")


