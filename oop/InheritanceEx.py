class shape:

    def __init__(self,type): #constructor
        print("inside shape")
        self.type = type

    def draw(self):
        print("Drawing shape")

    def area(self):
        print("area not implemented")
        # raise Exception("area not implemented")


class Rectange(shape):
    def __init__(self,type,length, breadth):
        print("inside rectangle")
        super().__init__(type)
        self.__length = length
        self.__breadth = breadth

    def draw(self):
        print("drawing rect")

    def area(self):
        return self.__length * self.__breadth



class Square(Rectange):
    def __init__(self,side):
        print("inside square")
        super().__init__("kjhjhj",side,side)

s = Square(4)
print("square is::")
print(s.area())

#ceating object
# r = Rectange("rect",12,10)
# print(r.area())
#
#
# s=shape()
# print()
# s.draw()
