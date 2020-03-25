# Python implements Object Oriented Programming using CLASSES
# Classes can be defined using following index
class className:

    def __init__(self,param):
        self.param = param

    def someMethod(self):
        print(self.param)

#end of class

class animal:

    def __init__(self,breed):
        self.breed = breed

    def printBreed(self):
        print(self.breed)

dog = animal("Lab")
dog.printBreed()
