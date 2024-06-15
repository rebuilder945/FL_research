def max_number_from_list(lst):
    sorted_lst = sorted(lst, reverse=True)
    result = ''.join(map(str, sorted_lst))
    return int(result)
input_list = [0, 1, 2, 3, 2]
result = max_number_from_list(input_list)
print(result)
