input_list = list(map(int,input().split(',')))
n, m = map(int, input().split(','))

if n >= len(input_list):
    print('error')
else:
    element = input_list[n]
    input_list.extend([element] * m)
    print(input_list)
