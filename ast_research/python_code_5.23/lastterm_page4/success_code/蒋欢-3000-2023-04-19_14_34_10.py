a=eval(input())
b=sum(a)/len(a)
c='{:.2f}'.format(b)
d=c.split('.')
if float(d[1]) in range(11):
    d.append('0')
else:
    pass
print(d)
