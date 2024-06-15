lst_str = input()
lst = eval(lst_str)
max_num = max(lst)
min_num = min(lst)
lst = [num for num in lst if num != max_num and num != min_num]
print(lst)
