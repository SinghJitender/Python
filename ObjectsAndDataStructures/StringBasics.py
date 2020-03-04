# Strings in python can be declare in SingleQuotes - ' ' or double quotes - " ". Both the examples below are correct

a = 'Hello World'
b = "Hello World"

print(a+" "+b)

# len() function to find length of string
a = len(b)
print(a)

# indexing in string. Character at specific index can be retrived by using [index] after the string. Example below

string = "I am a Developer"
print(string[0]) #Prints - I
# We can also use negative index to print characters from end of string,
# meaning index = -1 will represent last character and so on
print(string[-1]) #Prints - r