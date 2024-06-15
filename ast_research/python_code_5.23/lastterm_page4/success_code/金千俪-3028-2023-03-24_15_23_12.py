n,m,l=eval(input())
lst=[n]
for i in range(m-1):
    a=n+l
    lst.append(a)
    l=n+l
print(lst)
