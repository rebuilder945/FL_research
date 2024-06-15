a=eval(input())
n=a+1
d=range(1,n)
b=list(d)

for x in b:
    e=b.index(x)
    if e==0:
        continue
    else:
        b[e-1],b[e]=b[e],b[e-1]
print(b)
    


