import random


lst = [random.randint(-5, 5) for i in range(10)]
print(lst)
def normal_list(lst):
    max_num = max(lst, key=abs)
    for i, elem in enumerate(lst):
        lst[i] = elem / max_num
    print(lst)

print(normal_list(lst))