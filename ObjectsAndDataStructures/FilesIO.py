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