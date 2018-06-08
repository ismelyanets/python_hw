input_data = input('Enter any five-digit number:')
result = 1
for i in input_data:
    if not input_data.isnumeric():
        print('Invalid data!')
        break
    if len(input_data) != 5:
        print('Invalid data!')
        break
    i = int(i)
    if i % 2 != 0:
        result *= i
print(result)