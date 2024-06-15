n,m,l=eval(input())
lst=[n]
a=n
for i in range(m-1):
    a+=l
    lst.append(a)
print(lst)
