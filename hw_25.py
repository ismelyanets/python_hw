import random


list_to_shuffle = [i for i in range(1, 100) if i % 2 != 0]
print('-------------')
print('ID:', id(list_to_shuffle))
print('-------------')
print(list_to_shuffle)


def shuffle_list(list_to_shuffle):
    """
    Shuffle list *IN PLACE*
    :param list_to_shuffle:
    :return:
    """
    for i in range(1, len(list_to_shuffle) - 1):
        j = random.randrange(0, i)
        list_to_shuffle[j], list_to_shuffle[i] = list_to_shuffle[i], list_to_shuffle[j]

    print(list_to_shuffle, id(list_to_shuffle))



print(shuffle_list(list_to_shuffle))
