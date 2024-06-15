nn=eval(input())
a=list(nn)
b={}
for x in a:
    b[x]=a.count(x)
print(b)
