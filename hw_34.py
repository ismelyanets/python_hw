import random


class Godzilla():

    def __init__(self, weight):
        self.weight = weight

    def eat(self, man):
        limit_stomach = (0.9 * self.weight)
        fill_stomach_volume = 0
        while fill_stomach_volume < limit_stomach:
            if (fill_stomach_volume + man) <= limit_stomach:
                fill_stomach_volume += man
                print('Current volume %d, man = %d' % (fill_stomach_volume, man))
            else:
                print('I am full and can not eat people anymore')
                break

a = Godzilla(200)

print(a.eat(random.randint(30, 75)))




