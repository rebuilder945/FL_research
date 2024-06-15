u,v,x,y = input().split(" ")
z=int((int(v)+int(x)+int(y))/3)
list=['%.2f'%int(v),'%.2f'%int(x),'%.2f'%int(y)]
list.sort()
print(u," ".join(map(str,list)),'%.2f'%(z))

