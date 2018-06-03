def print_mult_table(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print("%10d" % i, '*',  j, '=',  (i * j), end='')
        print()


print_mult_table(5, 5)
