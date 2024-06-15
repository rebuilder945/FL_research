n=eval(input())
ls=list(range(1,n+1))
a=ls[0]
for i in range(1,n):
    ls[i-1]=ls[i]
ls[n-1]=a
print(ls)
