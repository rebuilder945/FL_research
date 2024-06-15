n=eval(input())
v=[x for x in range(1,n+1)]
a=v.copy()
for x in range(0,n):
    if x==n-1:
       a[x]=v[0]
    else:
        a[x]=v[x+1]
print(a)
    


    

