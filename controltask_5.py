import math


number_1 = 10
def closer_to_10 (a, b):
    distance_a = math.fabs(10 - a)
    distance_b = math.fabs(10 - b)
    if distance_a > distance_b:
        return b
    if distance_a < distance_b:
        return a
    else:
        return a, b

print(closer_to_10(8.5, 8.75))
