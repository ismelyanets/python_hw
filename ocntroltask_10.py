matrix = [[3, 8, 7],
          [5, 9, 6],
          [2, 6, 7]]


def saddle_elem(matrix):
    count = 0
    for i in matrix:
        if i.count(min(i)) == 1:
            min_elem = i.index(min(i))
            min_list = []
            for j in matrix:
                min_list.append(j[min_elem])
            if min_list.count(max(min_list)) == 1 and min(i) == max(min_list):
                result = (str(min_list.index(max(min_list))), str(min_elem))
                count += 1
        if count > 0:
            return result
    if count == 0:
        return False

print(saddle_elem(matrix))