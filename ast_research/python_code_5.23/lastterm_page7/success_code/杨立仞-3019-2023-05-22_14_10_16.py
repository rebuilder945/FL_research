a,b,c,d=input().split()
b=int(b)
c=int(c)
d=int(d)
e=[b,c,d]
e.sort(reverve=True)
avg=(b+c+d)/3
print("{} {:.2f} {:.2f} {:.2f} {:.2f} ".format(a,e[0],e[1],e[2],avg))
