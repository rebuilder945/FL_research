lst = eval(input())
lst_max = max(lst)
lst_min = min(lst)
num_max = lst.count(lst_max)
num_min = lst.count(lst_min)
if (lst_max == lst_min):
    print([])
else:
    for i in range(num_max):
        lst.remove(lst_max)
    for x in range(num_min):
        lst.remove(lst_min)
    print(lst)
