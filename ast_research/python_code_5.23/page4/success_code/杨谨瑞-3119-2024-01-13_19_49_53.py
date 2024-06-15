input_str = input()
orig_list = eval(input_str)
result_list = []
for i, item in enumerate(orig_list):
    if item in orig_list[i+1:]:
        continue
    result_list.append(item)
print('[', end='')
print(*result_list, sep=', ', end='')
print(']')

