name=input()
mark=eval(input())
lt=name.split(sep=",")
ii=[]
l=len(mark)
z=list()
for i in range(l):
    a=lt[i]
    b=mark[i]
    ii.append(a)
    ii.append(b)
    z.append(ii)
print(z)


