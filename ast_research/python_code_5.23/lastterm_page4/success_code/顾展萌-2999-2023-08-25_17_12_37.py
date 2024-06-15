lst = input().split()
n,m= input().split()
n = int(n)
m = int(m)
if n < m:
    sEx = lst.pop(m)
    lst.insert(n,sEx)
    Sex = lst.pop(n+1)
    lst.insert(m,Sex)
elif m<n:
    sEx = lst.pop(n)
    lst.insert(m,sEx)
    Sex = lst.pop(m+1)
    lst.insert(n,Sex)
else:
    pass
print(lst)

