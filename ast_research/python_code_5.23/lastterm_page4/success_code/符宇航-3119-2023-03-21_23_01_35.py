lst = eval(input())
lst1 = lst.copy()
for i in lst1:
    n = lst.count(i)
    if n>=2:
        for x in range(n-1):
            lst.remove(i)
print(lst)
