input_list = input().strip('[]')
num_list = list(map(int, input_list.split(',')))
num_list.sort(key=lambda x: 1 if x == 0 else 0)
print(num_list)
