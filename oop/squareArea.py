

class Rectangle:
    #constructer
    def __init__(self,type):
        self.type = type

    def area(self):
        print("inside base class")


class Square(Rectangle): #inheriting base class(Recvtangle)
    def __init__(self,type,length, breadth):
        super().__init__(type)
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

s = Square("square",10,10)
print(s.area())

