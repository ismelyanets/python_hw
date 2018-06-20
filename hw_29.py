import random
import string


def gen_password():
    encode_lower = string.ascii_lowercase
    encode_upper = string.ascii_uppercase
    encode_num = string.digits
    r = '_'
    password = ''
    for i in range(2):
        password += (random.choice(encode_lower) + random.choice(encode_upper) + random.choice(encode_num) + random.choice(r))
    return password

print(gen_password())



