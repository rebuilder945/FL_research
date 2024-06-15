lst_str = input()
lst = eval(lst_str)
new_lst = []
zero_lst = []
for num in lst:
    if num == 0:
        zero_lst.append(num)
    else:
        new_lst.append(num)
new_lst.extend(zero_lst)
print(new_lst)
