# Not meant to be instantiated but always extended
# Way to implement polymorphism strictly

# Animal is an abstract class
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Must be implemented in base class")

class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self.name)
        self.name = name

    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self.name)
        self.name = name

    def speak(self):
        print("MEOW!")


