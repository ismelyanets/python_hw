a = [[3, 8, 7],
     [5, 9, 6],
     [2, 6, 7]]

x = [x[0] for x in a]
x_1 = [x[1] for x in a]
x_2 = [x[2] for x in a]


q = sorted(x)
q1 = sorted(x_1, reverse=True)
q2 = sorted(x_2)
mat = [q, q1, q2]

for y in range(len(mat)):
     e = [e[y] for e in mat]
     print(e)
