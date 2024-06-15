lst_str = input()
lst = eval(lst_str)
avg = sum(lst) / len(lst)
if avg.is_integer():
    print(int(avg))
else:
    print('%.2f' % avg)
