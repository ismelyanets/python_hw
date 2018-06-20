def gen_primes(n):
    num_lst = [0] * n
    for i in range(n):
        num_lst[i] = i

    y = 2
    while y < n:
        if num_lst[y] != 0:
            j = y * 2
            while j < n:
                num_lst[j] = 0
                j = j + y
        y += 1

    primes_lst = []
    for i in num_lst:
        if num_lst[i] != 0:
            primes_lst.append(num_lst[i])


    return primes_lst
print(gen_primes(100))