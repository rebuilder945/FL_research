lst = eval(input())
if '0' in lst:
    for i in lst:
        lst.remove(0)
        lst.append(0)
else:
    pass
print(lst)
