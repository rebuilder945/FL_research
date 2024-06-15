a=eval(input())
b=sum(a)/len(a)
c='{:.2f}'.format(b)
d=c.split('.')
if float(d[1]) in range(1,11):
    d.append('0')
    d=str(d[:])
    d=float(d)
else:
    d=c
print(d)
