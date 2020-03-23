# Not meant to be instantiated but always extended
# Way to implement polymorphism strictly

# Animal is an abstract class
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Must be implemented in base class")

class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOW!")

dog = Dog("Vodafone")
cat = Cat("Badass")

print(type(dog))
print(type(cat))

for obj in [dog,cat]:
    obj.speak();
