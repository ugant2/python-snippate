


# Magic methods or dunders are special methods which
# have double underscores at the beginning and end of their names.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other, last):
        return Vector2D(self.x + other.x + last.x, self.y + other.y + last.y)

# objects and printing\
first = Vector2D(2,9)
second = Vector2D(5,4)
third = Vector2D(5,4)
result = first + second + third
print(result.x)
print(result.y)