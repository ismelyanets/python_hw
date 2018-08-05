import random


class Godzilla():
    LIMIT = 0.9

    def __init__(self, weight, fill_stomach_volume=0):
        self.weight = weight
        self.limit_stomach = (self.LIMIT * weight)
        self.fill_stomach_volume = fill_stomach_volume



    def eat(self, man):
        if (self.fill_stomach_volume + man) <= self.limit_stomach:
            self.fill_stomach_volume += man
            print('Current volume %d, man = %d' % (self.fill_stomach_volume, man))
        else:
            print('I am full and can not eat people anymore')


a = Godzilla(200)

print(a.eat(random.randint(30, 75)))
print(a.eat(random.randint(30, 75)))
print(a.eat(random.randint(30, 75)))
print(a.eat(random.randint(30, 75)))
print(a.eat(random.randint(30, 75)))