import random

lst = [random.randint(-1, 1) for i in range(11)]
print(lst)

def calc_frequency(lst):
    count_ = 0
    count_0 = 0
    count_1 = 0
    for elem in lst:
        if elem == -1:
            count_ += 1
        elif elem == 0:
            count_0 += 1
        else:
            count_1 += 1
    print(count_, count_0, count_1)
    if count_ == count_0 or count_ == count_1 or count_0 == count_1:
        return 'None'
    elif count_ > count_0 and count_ > count_1:
        return 'count_'
    elif count_0 > count_ and count_0 > count_1:
        return 'count_0'
    else:
        return 'count_1'

print(calc_frequency(lst))
