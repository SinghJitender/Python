class Dog:
    def __init__(self):
        print("I'm a Dog")
    def speak(self):
        print("WOOF!")


class Cat:
    def __init__(self):
        print("I'm a Cat")

    def speak(self):
        print("MEOW!")

def pet_speak(pet):
    # speak() method is called based upon the type of object passed to the method.
    # Here speak method represents Polymorphism - (One Name, Many Forms)
    pet.speak()

lab = Dog()
pussy = Cat()

pet_speak(lab)
pet_speak(pussy)
