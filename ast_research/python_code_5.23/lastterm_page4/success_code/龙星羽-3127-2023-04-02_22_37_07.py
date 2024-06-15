n=eval(input())
ls=[x for x in range(1,n+1)]
for i in range(0,n):
    if i<n-1:
        ls[i]=ls[i+1]
    else:
        ls[n-1]=1
print(ls)

