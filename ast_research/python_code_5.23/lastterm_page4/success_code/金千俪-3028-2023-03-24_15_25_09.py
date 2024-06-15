n,m,l=eval(input())
lst=[n]
for i in range(m-1):
    lst.append(n+l)
    n=n+l
print(lst)
