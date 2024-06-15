m=input().split()
o=m[0]
m.pop(0)
n=[int(x) for x in m]
n.sort()
a=float(n[0])
b=float(n[1])
c=float(n[2])
d=(a+b+c)/3
print('%s %.2f %.2f %.2f %.2f'%(o,a,b,c,d))

