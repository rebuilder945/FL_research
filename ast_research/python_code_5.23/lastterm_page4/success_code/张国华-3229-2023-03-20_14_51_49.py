lst_str = input()
lst = eval(lst_str)
res = []
for num in lst:
    if lst.count(num) == 1:
        res.append(num)
if res:
    res.sort()
    print(','.join(str(num) for num in res))
else:
    print(False)

