input_list = list(map(int, input().strip('[]').split(',')))

input_list.sort(reverse=True)

max_number = ''.join(map(str,input_list))

print(int(max_number))
