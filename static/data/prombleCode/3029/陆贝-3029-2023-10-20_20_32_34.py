name=input()
mark=eval(input())
lt=name.split(sep=",")
ii=[]
l=len(mark)
for i in range(l):
    a=lt[i]
    b=mark[i]
    z=a+b
    ii.append(z)
print(ii)


