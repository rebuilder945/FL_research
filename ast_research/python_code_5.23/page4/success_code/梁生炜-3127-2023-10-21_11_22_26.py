n=int(input())
ls=list(range(1,n+1))
ls2=ls.copy()
for i in range(n-1):
    ls2[i]=ls[i+1]
ls2[n-1]=ls[0]
print(ls2)
