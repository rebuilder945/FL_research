n=eval(input())
a=[x for x in range(1,n+1)]
b=[]
for x in a:
    if x==n:
        x=b.append(x)

    else:
        x=x+1
        b.append(x)
print(b)
