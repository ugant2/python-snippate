

#
# The expression x + y is translated into x.__add__(y).
# However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called.
# There are equivalent r methods for all magic methods just mentioned.

class SuperString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SuperString("spam")
hello = SuperString("Hello world!")
print(spam/hello)