lst = eval(input())
lst_max = max(lst)
lst_min = min(lst)
num_max = lst.count(lst_max)
num_min = lst.count(lst_max)
if (num_max == num_min):
    print([])
else:
    for num in range(lst_max):
        lst.remove(lst_max)
    for num in range(lst_min):
        lst.remove(lst_min)
    print(lst)
