


class Cat:
    # constructor
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

    # def __str__(self, color, legs):
    #     return "{} {}".format(self.color, self.legs)
    def __str__(self):
        return str("This cat has " + self.color + " color "+ "and " + str(self.legs)+ " legs")

# objects
flexi = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

print(flexi.color, flexi.legs)
print(rover.color, rover.legs)
print(stumpy.color, stumpy.legs)