lst = eval(input())
mx = max(lst)
mn = min(lst)
lst1 = lst.copy()
for x in lst:
    if x == mx:
        lst1.remove(x)
    elif x == mn:
        lst1.remove(x)
print(lst1)

