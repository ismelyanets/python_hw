lst = [1, 2, 3, 4, 5, 9, 6, 7]
print('-------------')
print('ID:', id(lst))
print(lst)
print('-------------')

a = lst.index(min(lst))
b = lst.index(max(lst))
lst[a], lst[b] = lst[b], lst[a]


print(lst, id(lst))