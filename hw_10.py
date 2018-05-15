date_life = 'Marcus Aurelius*121-04-26*180-03-17'
date_life_lst = date_life.split('*')
name = date_life_lst[0]
date_born = date_life_lst[1]
date_died = date_life_lst[2]
date_born_lst = date_born.split('-')
date_died_lst = date_died.split('-')
year_born = int(date_born_lst[0])
year_died = int(date_died_lst[0])
years_life = str(year_died - year_born)
lifetime = (name + ',' + years_life)
print(lifetime)