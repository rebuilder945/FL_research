n,m,l=input().split(',')
n=int(n)
m=int(m)
l=int(l)
lst=[x for x in range(n,m*l+n,l)]
print(lst)
