# classes can be extended to implement inhertance

class Animal:
    def __init__(self):
     print("Animal Created")

    def who_am_i(self):
     print("I'm an animal")

    def eat(self):
        print("I'm eating")

# Class Dog extends Class Animal and all its methods (Animal Class) can now be called using Dog class object
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def brak(self):
        print("Barking!!")

    # Method Overriding
    def who_am_i(self):
        print("I'm a Dog.")

dog_obj = Dog()
# Dog's class own method
dog_obj.brak()
# Overridden method from animal class
dog_obj.who_am_i()
# Animal class method
dog_obj.eat()