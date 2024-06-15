a=input().split(',')
b=list(a)
n=b[0]
m=b[1]
l=b[2]
k=n+(m-1)*l
list=list(range(n,k+1,l))
print(list)
