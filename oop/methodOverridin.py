




# If a class inherits from another with the same attributes or methods, it overrides them.

class Wolf: # Wolf is a super class
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def bark(self):
        print("Grr")


class Dog(Wolf): #Dog is a sub-class
    #method overriding
    def bark(self):
        print("Woof")


#objects
husky = Dog("Husky", "brown")
print(husky.name, husky.color)
husky.bark()