import random


class Godzilla():
    FILL_STOMACH_VOLUME = 0

    def __init__(self, weight):
        self.weight = weight



    def eat(self, man):
        limit_stomach = (0.9 * self.weight)
        if (self.FILL_STOMACH_VOLUME + man) <= limit_stomach:
            self.FILL_STOMACH_VOLUME += man
            print('Current volume %d, man = %d' % (self.FILL_STOMACH_VOLUME, man))
        else:
            print('I am full and can not eat people anymore')


a = Godzilla(200)

print(a.eat(random.randint(30, 75)))
print(a.eat(random.randint(30, 75)))
print(a.eat(random.randint(30, 75)))
print(a.eat(random.randint(30, 75)))
print(a.eat(random.randint(30, 75)))