n,m,l=map(int,eval(input()).split(','))
lst=[n]
for i in range(m):
    n+=l
    lst.append(n)
print(lst)
