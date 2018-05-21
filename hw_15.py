import math


def circles_intersect(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if distance <= (r1 + r2) and distance >= math.fabs(r1 - r2) or (distance == 0 and r1 == r2):
        return True
    else:
        return False

print(circles_intersect(0, 0, 5, 0, 0, 4))

