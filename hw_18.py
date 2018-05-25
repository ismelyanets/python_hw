def sum_symbol_codes(first, last):
    code_first = ord(first)
    code_last = ord(last)
    count_code = (code_last - code_first) + 1
    total_sum = (code_first + code_last)*count_code / 2
    return int(total_sum)

print(sum_symbol_codes('x', 'z'))
