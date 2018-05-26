def get_max_digit(number):
    max_num = number % 10
    number = number // 10
    while number > 0:
        if number % 10 > max_num:
            max_num = number % 10
        number = number // 10
    return max_num

print(get_max_digit(89999999999))



