# We will see how we can iplement or use Python's inbuilt methods in our own class like - print, len, etc

class Book():
    def __init__(self,author,book,pages):
        self.author = author
        self.book = book
        self.pages = pages

    # toString method of Python. Returns String representation of class
    def __str__(self):
        return f"{self.author} by {self.book}"

    def __len__(self):
        return self.pages

book1  = Book("Jitender","Python Advance to Null",200)
# __str__ method being called automatically
print(book1)
print(len(book1))

# To delete the variable from memory use 'del variable_name'
del book1



