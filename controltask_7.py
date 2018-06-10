def sum_fibonacci(n):
    fibo_list = []
    fibo_1 = 0
    fibo_2 = 1
    for i in range(n):
        fibo_1, fibo_2 = fibo_2, fibo_1 + fibo_2
        fibo_list.append(fibo_1)
    return sum(fibo_list)


print(sum_fibonacci(10))
