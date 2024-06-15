n=int(input())
ls=list(range(n+1))
ls2=ls.copy()
for i in range(n-1):
    ls2[i]=ls[i+1]
ls2[0]=ls[n]
print(ls2)
