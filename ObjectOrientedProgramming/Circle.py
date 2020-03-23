class Circle:
    pie = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius**2*self.pie

    def circumference(self):
        print(f"Circumference of circle : {2*self.radius*self.pie} ")

obj = Circle(1)
obj.circumference()