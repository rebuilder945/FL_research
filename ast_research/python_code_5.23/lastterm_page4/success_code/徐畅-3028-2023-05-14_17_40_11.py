n,m,l=map(int,input().split(','))
lst=[n]
for i in range(m-1):
    n+=l
    lst.append(n)
print(lst)
