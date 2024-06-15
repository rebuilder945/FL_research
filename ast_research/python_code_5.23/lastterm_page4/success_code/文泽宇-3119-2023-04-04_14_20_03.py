lst = eval(input())
lst1 = []
for x in lst:
    if x not in lst1:
        lst1.append(x)
    else:
        lst1.remove(x)
        lst1.append(x)
print(lst1)
