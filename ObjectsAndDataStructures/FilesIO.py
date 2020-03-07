# to open a file, document, audio, picture, etc 'open()' method will be used.
file = open('test')
print(file.read())
file.seek(0) # reset the cursor to Zero i.e. start of file.
print(file.read())
file.seek(0)
print(file.readlines()) # returnes list of elements.

# it is necessary to close the file object when you are done so that i some other program is using it, it works as intended
# one way to close is
file.close();

# other way is that you use following syntax
with open('test') as myfile:
    contents = myfile.read()
# using the above syntax it automaticallys closes the file object once you are out of the given code block
print(contents)

# file is always open in read mode by default. to write to a file we have to open it in write mode.
# we can pass the 'mode' is 'open()' method to open the file in specific mode like we can pass 'w' for writing , 'a' for appending, etc
# all mode - 'r' , 'w', 'a', 'r+' (reading and writing), 'w+' (writing and reading. Either overwrites existing file or create new file )

with open('test','w') as myfile:
    myfile.write(contents + "This file is overwritten.")

with open('test','a') as myfile:
    myfile.write(contents + "Contents now are appended.")

