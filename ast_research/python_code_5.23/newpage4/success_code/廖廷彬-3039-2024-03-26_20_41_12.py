input_list = eval(input())
max_value = max(input_list)
min_value = min(input_list)
output_list = [x for x in input_list if x != max_value and x != min_value]
print(output_list)
