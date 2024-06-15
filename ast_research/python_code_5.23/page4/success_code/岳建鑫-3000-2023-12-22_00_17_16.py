input_str = input()
num_list = input_str.strip('[]').split(',')
num_list = [int(num) for num in num_list]
average = sum(num_list) / len(num_list)
print('{:.2f}'.format(average))

