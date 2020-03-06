# to open a file, document, audio, picture, etc 'open()' method will be used.
file = open('test')
print(file.read())
file.seek(0) # reset the cursor to Zero i.e. start of file.
print(file.read())