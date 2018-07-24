class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def include(self, x, y):
        if (x - self.a)**2 + (y - self.b)**2 <= (self.r)**2:
            print('This point inside the circle')
        else:
            print('This point is not inside the circle')


class Dot:
    def __init__(self, x, y):
        self.dot = (x, y)

d = Dot(0, 5)
t = Circle(3, 4, 3)
print(t.include(0, 5))

