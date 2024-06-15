n=int(input())
ls1=[x for x in range(1,n+1)]
a=ls1[0]
for i in range(1,n):
    ls1[i-1]=ls1[i]
ls1[n-1]=a
print(ls1)
