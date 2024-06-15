s = input().split(' ')
m,n = input().split(' ')
a = int(m)
b = int(n)
lst = list(s)
lst1 = lst.copy()
lst1[a] = lst[b]
lst1[b] = lst[a]
print(lst1)
