class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def include(self, d):
        if (d.x - self.a)**2 + (d.y - self.b)**2 <= (self.r)**2:
            return True
        else:
            return False


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

d = Dot(3, 5)
t = Circle(3, 4, 3)
print(t.include(d))

