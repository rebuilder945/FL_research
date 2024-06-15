n,m,l=[int(x)for x in input().split(',')]
lst=[]
for x in range(m):
    lst.append(n)
    n+=l
print(lst)
