import math


def cone_square_and_volume(radius, height):
    cone_square = float(math.pi*radius*(radius + math.sqrt(radius ** 2 + height ** 2)))
    cone_volume = float((math.pi * height * (radius ** 2)) / 3)
    return cone_square, cone_volume

print(cone_square_and_volume(3, 4))
print(cone_square_and_volume(7, 11))


#return 'Площадь конуса %.2f:' % cone_square, 'Объем конуса: %.2f' % cone_volume