lst1 = eval(input())
for a in lst1:
    if lst1.count(a) > 1:
        lst1.remove(a)
    else:
        break
print(lst1)


