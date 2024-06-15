n=eval(input())
lis=list(range(1,n+1))
a=lis[n-1]
b=lis[0]
for i in range(len(lis)):
    if i>=1:
        lis[i-1]=lis[i]        
    else:lis[n-1]=a
lis[n-1]=b
print(lis)
