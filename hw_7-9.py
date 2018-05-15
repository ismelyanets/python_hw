#-------task_7-----------
american_date = '05.17.2016'
american_date_lst = american_date.split('.')
month = (american_date_lst[0])
day = american_date_lst[1]
year = american_date_lst[2]
european_date = day + '.' + month + '.' + year
print(european_date)

#--------task_8-------------
name_surname = 'Mark Zuckerberg'
name_lst = name_surname.split(' ')[::-1]
surname_name = ' '.join(name_lst)
print(surname_name)

#--------task_9-------------
snake_case = 'employee_first_name'
case1 = snake_case.split('_')
word1 = case1[0]
word2 = case1[1]
word3 = case1[2]
camel_case = word1.capitalize()+word2.capitalize()+word3.capitalize()
print(camel_case)