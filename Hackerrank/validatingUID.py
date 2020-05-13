'''
ABCXYZ company has up to  employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.
A valid UID must follow the rules below:
It must contain at least  uppercase English alphabet characters.
It must contain at least  digits ( - ).
It should only contain alphanumeric characters ( - ,  -  &  - ).
No character should repeat.
There must be exactly  characters in a valid UID.
Input Format
The first line contains an integer , the number of test cases.
The next  lines contains an employee's UID.

Output Format
For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input
2
B1CD102354
B1CDEF2354

Sample Output
Invalid
Valid

Explanation
B1CD102354:  is repeating → Invalid
B1CDEF2354: Valid

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
num = "0123456789"
smallAplha = "abcdefghijklmnopqrstuvwxyz"
bigAplha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for x in range(int(input())):
    s = input()
    digits = 0
    uppercasechar = 0
    partials = ""
    if(len(s)==10):
        flag = True
        for ch in s:
            if(ch in partials):
                print("Invalid")
                flag = False
                break
            elif(ch in num):
                digits+=1
            elif(ch in bigAplha):
                uppercasechar +=1
            elif(ch not in bigAplha and ch not in smallAplha and ch not in num):
                print("Invalid")
                flag = False
                break
            partials += ch
        if (digits>=3 and uppercasechar>=2 and flag == True):
             print("Valid")
        elif ( (digits<3 or uppercasechar<2 ) and flag == True ):
            print("Invalid")
    else :
        print("Invalid")
