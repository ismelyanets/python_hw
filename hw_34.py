import random


class Godzilla():
    stomach_volume = 1000


    def eat(self):
        limit_stomach = (0.9 * self.stomach_volume)
        fill_stomach_volume = 0
        while fill_stomach_volume < limit_stomach:
            man = random.randint(30, 75)
            if (fill_stomach_volume + man) <= limit_stomach:
                fill_stomach_volume += man
                print('Current volume %d, man = %d' % (fill_stomach_volume, man))
            else:
                print('I am full and can not eat people anymore')
                break


a = Godzilla()

print(a.eat())


