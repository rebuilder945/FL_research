n=eval(input())
v=[x for x in range(1,n+1)]
a=v.copy()
for x in range(0,n):
    if x==0:
       a[n-1],a[x]=v[x],v[x+1]
    else:
        a[x]=v[x-1]
print(a)
    


    

