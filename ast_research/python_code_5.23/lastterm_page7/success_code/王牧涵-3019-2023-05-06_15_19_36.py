u,v,x,y = input().split(" ")
v=float(v)
x=float(x)
y=float(y)
z=float((int(v)+int(x)+int(y))/3)
list=[float('%.2f'%float(v)),float('%.2f'%float(x)),float('%.2f'%float(y))]
list.sort(reverse=True)
print(u," ".join(map(str,list)),'%.2f'%(z))

