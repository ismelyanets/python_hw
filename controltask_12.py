import random


spisok = []
for i in range(2, 10):
    for j in range(i , 10):
            print(['{} x {} = {}'.format(i, j, i*j)], end=' ')
            spisok += ['{} x {} = {}'.format(i, j, i * j)]
    print()

def teacher_choice(spisok):
    num_15 = random.sample(spisok, 15)
    return num_15

print(teacher_choice(spisok))
