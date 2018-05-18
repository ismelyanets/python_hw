#-------1---------------
def sum_of_digits(number):
    numb = str(number)
    result = int(numb[:1]) + int(numb[1:2]) + int(numb[2:])
    return result

print(sum_of_digits(358))


#--------2--------------
def sum_of_digits(number):
    n1 = number % 10
    n2 = number % 100 // 10
    n3 = number // 100
    result = n1 + n2 +n3
    return result

print(sum_of_digits(886))