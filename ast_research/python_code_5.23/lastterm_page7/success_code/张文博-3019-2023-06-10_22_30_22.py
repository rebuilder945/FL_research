m=input().split()
o=m[0]
m.pop(0)
m.sort()
a=float(m[0])
b=float(m[1])
c=float(m[2])
d=(a+b+c)/3
print('%s %.2f %.2f %.2f %.2f'%(o,a,b,c,d))

