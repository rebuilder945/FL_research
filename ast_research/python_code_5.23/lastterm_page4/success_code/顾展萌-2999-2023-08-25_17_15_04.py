lst = input().split()
n,m= input().split()
n = int(n)
m = int(m)
if 0<n < m:
    sEx = lst.pop(m)
    lst.insert(n,sEx)
    Sex = lst.pop(n+1)
    lst.insert(m,Sex)
elif 0<m<n:
    sEx = lst.pop(n)
    lst.insert(m,sEx)
    Sex = lst.pop(m+1)
    lst.insert(n,Sex)
elif n<m<0:
    sEx = lst.pop(n)
    lst.insert(m,sEx)
    Sex = lst.pop(m+1)
    lst.insert(n,Sex)
elif m<n<0:
    sEx = lst.pop(m)
    lst.insert(n,sEx)
    Sex = lst.pop(n+1)
    lst.insert(m,Sex)
else:
    pass

print(lst)

