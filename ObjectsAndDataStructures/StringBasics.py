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


# StepSize is another parameter that can be passed while doing the slicing of string
# It signifies the size of jump it will take to reach the next letter.
# Syntax - StringName[StartIndex:EndIndex:StepSize]
# Example - if string = "123456" and step size is 2. - string[::2] it will skip every alternate character
# Output will be - 135.

thirdString = "123456789"
print(thirdString[::2]) # skips every 2nd character in string starting from index 0 to end
print(thirdString[2::3]) # start with index 2 uptill end and print every 3rd character and skips the rest
print(thirdString[:7:4]) # start with 0 and end at 7. prints every 4th character
print(thirdString[2:5:2]) # start at 2 end at 5 and prints every 2nd character
print(thirdString[::-1]) # trick to reverse the string
