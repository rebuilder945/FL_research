lst = eval(input())
lst1 = lst
for i in lst1:
    if lst.count(i)>1:
        lst.remove(i)
print(lst)

