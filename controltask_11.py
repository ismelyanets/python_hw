import random
import pprint

a = [[random.randint(1, 9) for _ in range(5)]
     for _ in range(5)]

pprint.pprint(a)
mat = []
for i in range(len(a)):
    x = [x[i] for x in a]
    if i % 2 == 0:
        q = sorted(x)
    else:
        q = sorted(x, reverse=True)
    mat += [q]

for y in range(len(mat)):
    e = [e[y] for e in mat]
    print(e)