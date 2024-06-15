input_list = list(map(int, input().split(','))
n, m = map(int, input().split(',')
if abs(n) < len(input_list):
    if n >= 0:
        element = input_list[n]
    else:
        element = input_list[n + len(input_list)]
        new_list = input_list + [element] * m
    print(new_list)
else:
    print("error")
