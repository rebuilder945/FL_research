input_list = eval(input().strip())
max_number = int(''.join(map(str, sorted(input_list, reverse=True))))
print(max_number)


