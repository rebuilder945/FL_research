a=input().split(',')
b=list(a)
n=int(b[0])
m=int(b[1])
l=int(b[2])
k=n+(m-1)*l
list=list(range(n,k+1,l))
print(list)
