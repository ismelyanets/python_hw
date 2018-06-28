import csv
from collections import Counter


def distribution_of_survivals(passengers, field_name):
    f = open(passengers, "r")
    list_dicts = [row for row in csv.DictReader(f)]
    f.close()

    for data in list_dicts:
        count_pass = Counter(data[field_name] for data in list_dicts)
        surv_pass = Counter(data[field_name] for data in list_dicts if data['Survived'] == '1')


    for k in count_pass.keys():
        share_surv = ((surv_pass.get(k)) / (count_pass.get(k))) * 100
        print(field_name + ": " + k + " " + '%.2f' % (share_surv) + '%', end='    ')

distribution_of_survivals('titanic.csv', 'Sex')