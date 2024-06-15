n,m,l=input().split(",")
n=int(n)
m=int(m)
l=int(l)
k=n+(m-1)*1
lst=list(range(n,k+1,l))
print(lst)
