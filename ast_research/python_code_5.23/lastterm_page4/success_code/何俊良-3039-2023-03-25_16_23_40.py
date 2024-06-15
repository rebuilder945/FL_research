lst = eval(input())
max_val = max(lst)
min_val = min(lst)
new_lst = [x for x in lst if x != max_val and x != min_val]
print(new_lst)

