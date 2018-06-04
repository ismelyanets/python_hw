list_of_enrollees = ['Kris Barns', 'Bob Tornton', 'James Oneill', 'Andreas Art', 'Her Zer']


def group_by_surname(list_of_enrollees):
    group_1 = 0
    group_2= 0
    group_3 = 0
    group_4 = 0

    for i in range(len(list_of_enrollees)):
        elem_list = list_of_enrollees[i]
        name_surname = elem_list.split()

        if 64 < ord(name_surname[1][0]) < 74:
            group_1 += 1
        elif 73 < ord(name_surname[1][0]) < 81:
            group_2 += 1
        elif 80 < ord(name_surname[1][0]) < 85:
            group_3 += 1
        elif 84 < ord(name_surname[1][0]) < 91:
            group_4 += 1
    return (group_1, group_2, group_3, group_4)

print(group_by_surname(list_of_enrollees))