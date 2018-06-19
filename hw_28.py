import string

str_to_encode = input("Введите строку: ")


def encode(str_to_encode):
    encoded_string = ""
    encode_table = string.ascii_lowercase + string.digits

    for i in str_to_encode:
        if i not in encode_table:
            encoded_string += i
            continue

        elem = (encode_table.index(i) + 5) % len(encode_table)
        encoded_string += encode_table[elem]

    return encoded_string


print(encode(str_to_encode))