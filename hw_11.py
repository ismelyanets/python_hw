import math


def degrees2radians(degrees):
    return (degrees * math.pi) / 180


cos_60 = math.cos(degrees2radians(60))
cos_45 = math.cos(degrees2radians(45))
cos_40 = math.cos(degrees2radians(40))
print('Cos угла 60 равен: %.2f' % cos_60 + ' ;' + 'Cos угла 45 равен: %.2f' % (
    cos_45) + ' ;' + 'Cos угла 40 равен: %.2f' % cos_40)


