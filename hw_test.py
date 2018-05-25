import random


def diff_even_odd(num_limit, lower_bound, upper_bound):
    sum_even = 0
    sum_odd = 0
    for i in range(num_limit):
        random_number = random.randint(lower_bound, upper_bound)
        print(random_number)
        if random_number % 2 == 0:
            sum_even += random_number
        elif random_number % 2 != 0:
            sum_odd += random_number
    sum_diff = sum_even - sum_odd
    return sum_diff

print(diff_even_odd(5, 2, 100))