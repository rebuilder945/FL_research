n=eval(input())
ls=[x for x in range(1,n+1)]
for i in range(n):
    if i==(n-1):
        ls[n-1]=ls[0]
    else:
        ls[i]=ls[i+1]
print(ls)
