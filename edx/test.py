

class Wild(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return self.x
    def getY(self):
        return self.y


X = 7
Y = 8
w1 = Wild(X, Y)
print(w1.getX())