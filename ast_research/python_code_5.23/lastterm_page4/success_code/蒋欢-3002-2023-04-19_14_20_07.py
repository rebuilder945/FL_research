a=eval(input())
b=sum(a)/len(a)
c="%.2f"%b
d=c.split('.')
if d[1]=='00':
    e=float(c)
    e=int(e)
else:
    e=c
print(e)
