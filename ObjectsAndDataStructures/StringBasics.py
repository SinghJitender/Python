# Strings in python can be declare in SingleQuotes - ' ' or double quotes - " ". Both the examples below are correct

a = 'Hello World'
b = "Hello World"

print(a+" "+b)

# len() function to find length of string
a = len(b)
print(a)

# indexing in string. Character at specific index can be retrieved by using [index] after the string. Example below

string = "I am a Developer"
print(string[0]) #Prints - I
# We can also use negative index to print characters from end of string,
# meaning index = -1 will represent last character and so on
print(string[-1]) #Prints - r

# substrings can be retrieved by passing starting and end index in [] seperated by : after the string
# example - stringName[startIndex:EndIndex]
# Note - value at endindex is not included in the string.
secondString = "abcdefghij";
print(secondString[2:]) # print string starting from index 2 up till end of string
print(secondString[:4]) # print string starting from index 0 up till index 4 (excluding value at index 4 i.e 'e')
print(secondString[3:6]) # print string starting from index 3 up till index 5 (excluding 6)
