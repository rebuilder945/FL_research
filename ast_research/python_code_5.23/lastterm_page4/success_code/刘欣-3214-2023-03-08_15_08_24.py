raw_list = eval(input())
raw_list_remove_zero = [item for item in raw_list if item != 0]
zero_list = [0] * (len(raw_list) - len(raw_list_remove_zero))
result = raw_list_remove_zero + zero_list
print(result)
