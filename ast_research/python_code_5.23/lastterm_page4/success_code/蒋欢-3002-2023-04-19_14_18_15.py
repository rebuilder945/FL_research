a=eval(input())
b=sum(a)/len(a)
c="%.2f"%b
d=c.split('.')
if d[1]=='00':
    e=int(c)
else:
    e=c
print(e)
