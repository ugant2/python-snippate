

# Inheritance provides a way to share functionality between classes.
# Imagine several classes, Cat, Dog, Rabbit and so on. Although they may
# differ in some ways (only Dog might have the method bark),
# they are likely to be similar in others (all having the attributes color and name).

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

# class Cat, Animla is a supar class
class Cat(Animal):
    def purr(self):
        print("Purr...")

# class Dog
class Dog(Animal):
    def bark(self):
        print("Woof!")


#objects
fido = Dog("Fido", "Brown")
print(fido.color, fido.name)
fido.bark()