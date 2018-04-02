


class Coordinte(object):
  def __init__(self,x ,y):
    self.x = x
    self.y = y
  def distance(self, other):
    x_diff_sq = (self.x - other.x)**2
    y_diff_sq = (self.y - other.y)**2
    return (x_diff_sq + y_diff_sq)**0.5

  def __str__(self):
    return "<" + str(self.x) + "," + str(self.y) + ">"

  def __sub__(self, other):
    return Coordinte(self.x - other.x, self.y - self.y)

# c = Coordinte(3,4)
# print(c)
# origin = Coordinte(0, 0)
# print(c.distance(origin))
# print(Coordinte.distance(c, origin))
# # print(type(c)) checks the type of c object
# print(isinstance(c, Coordinte))

c = Coordinte(5,2)
origin = Coordinte(0, 0)
dis = c - origin
print(dis)