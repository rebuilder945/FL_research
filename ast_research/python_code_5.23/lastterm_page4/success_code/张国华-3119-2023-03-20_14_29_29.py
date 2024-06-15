lst_str = input()
lst = eval(lst_str)
new_lst = []
for num in lst:
    if num not in new_lst:
        new_lst.append(num)
print(new_lst)

