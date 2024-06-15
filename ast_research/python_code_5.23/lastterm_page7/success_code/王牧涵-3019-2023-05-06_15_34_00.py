u,v,x,y = input().split(" ")
v=float(v)
x=float(x)
y=float(y)
z=float((int(v)+int(x)+int(y))/3)
list=[float('%.2f'%v),float('%.2f'%float(x)),float('%.2f'%float(y))]
list.sort(reverse=True)
d=(" ".join(map(str,list)))
a,b,c=d.split(" ")
print(u,'%.2f'%float(a),'%.2f'%float(b),'%.2f'%float(c),'%.2f'%(z))

