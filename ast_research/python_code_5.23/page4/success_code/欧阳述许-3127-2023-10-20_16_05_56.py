n=eval(input())
v=[x for x in range(1,n+1)]
a=v.copy()
for x in range(1,n+1):
    if x==1:
        a[x-1]=v[n-1]
    else:
        a[x]=v[x-1]
print[a]
    


    

