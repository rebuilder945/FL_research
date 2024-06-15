n=int(input())
ls1=[i+1 for i in range(n)]
for i in range(n-1):
    ls1[i]=ls1[i+1]
ls1[n-1]=1
print[ls1]
