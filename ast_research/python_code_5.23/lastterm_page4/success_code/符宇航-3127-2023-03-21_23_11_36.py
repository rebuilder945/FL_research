n = int(input())
lst = list(range(n+1))
lst1 = lst.copy()
for i in lst1:
    a = lst1[i]
    lst[i-1] = a
print(lst)
