import csv



def get_data_from_csv(filename):

    f = open(filename, "r")
    list_dicts = [row for row in csv.DictReader(f)]
    f.close()

    return list_dicts


data_lst = get_data_from_csv('titanic.csv')


print(data_lst)
count_sur_man = 0
count_sur_woman = 0
for data in data_lst:
    if data['Sex'] == 'male' and data['Survived'] == '1':
        count_sur_man += 1
    if data['Sex'] == 'female' and data['Survived'] == '1':
        count_sur_woman += 1
print('-------------------------------------')
print('Survived man: ', count_sur_man)
print('Survived woman: ', count_sur_woman)
print('-------------------------------------')

sur_cl_1 = 0
sur_cl_2 = 0
sur_cl_3 = 0
for data in data_lst:
    if data['Pclass'] == '1' and data['Survived'] == '1':
        sur_cl_1 += 1
    elif data['Pclass'] == '2' and data['Survived'] == '1':
        sur_cl_2 += 1
    elif data['Pclass'] == '3' and data['Survived'] == '1':
        sur_cl_3 += 1


print('-------------------------------------')
print('Survived 1 class: ', sur_cl_1)
print('Survived 2 class: ', sur_cl_2)
print('Survived 3 class: ', sur_cl_3)
print('-------------------------------------')


share_man = 0
share_woman = 0
for data in data_lst:
    if data['Sex'] == 'male':
        share_man += 1
    if data['Sex'] == 'female':
        share_woman += 1
print('-------------------------------------')
print('Share sur man: % .2f' % (count_sur_man / share_man))
print('Share sur woman: % .2f' % (count_sur_woman / share_woman))
print('-------------------------------------')

share_sur_cl_1 = 0
share_sur_cl_2 = 0
share_sur_cl_3 = 0
for data in data_lst:
    if data['Pclass'] == '1':
        share_sur_cl_1 += 1
    elif data['Pclass'] == '2':
        share_sur_cl_2 += 1
    elif data['Pclass'] == '3':
        share_sur_cl_3 += 1


print('-------------------------------------')
print('Share sur 1 class: % .2f' % (sur_cl_1 / share_sur_cl_1))
print('Share sur 2 class: % .2f' % (sur_cl_2 / share_sur_cl_2))
print('Share sur 3 class: % .2f' % (sur_cl_3 / share_sur_cl_3))
print('-------------------------------------')