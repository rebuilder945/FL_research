def remove_max_min(input_list):
    max_value = max(input_list)
    min_value = min(input_list)
    output_list = [x for x in input_list if x != max_value and x != min_value]
    print(output_list)

input_list = [1, 2, 3, 4, 5, 6, 1, 7, 7]
remove_max_min(input_list)

