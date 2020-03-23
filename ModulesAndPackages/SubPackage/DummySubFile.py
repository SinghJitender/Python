def dummyMethod():
    print("This is a dummy method")

# To see if file is being called directly or some other module.
# It has other uses as well. This is just for explanation
if __name__ == "__main__":
    print("DummySubFile.py is being called direclty")
else:
    print("DummySubFile.py called from some other class")