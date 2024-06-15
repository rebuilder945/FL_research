lst = eval(input())
a = max(lst)
b = min(lst)
lstl = lst.copy
for x in lst:
    if x==a or x==b:
        lstl.remove(x)
print(lstl)
