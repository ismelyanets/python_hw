import random


def diff_min_max(num_limit, lower_bound, upper_bound):
    max_num = lower_bound
    min_num = upper_bound
    for i in range(num_limit):
        random_number = random.randint(lower_bound, upper_bound)
        print(random_number)
        if random_number > max_num:
            max_num = random_number
        if random_number < min_num:
            min_num = random_number
    diff_sum = max_num - min_num
    return diff_sum



print(diff_min_max(10, 10, 100))



