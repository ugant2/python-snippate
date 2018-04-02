


#  Classes can have other methods defined to add functionality to them.
# Remember, that all methods must have self as their first parameter.
# Classes also have class attributes that can be either accessed by object or class itself
class Dog:
    legs = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color

    #class method
    def bark(self):
        print("Woof!")

#objects
fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()
print(fido.legs) # calss atributes accessed using objects

