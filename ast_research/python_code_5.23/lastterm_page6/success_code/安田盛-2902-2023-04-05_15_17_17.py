n=eval(input())
x=2
y=1
a=x/y
c=[a]
for i in range(n-1):
    b=y
    y=x
    x=x+b
    a=x/y
    c.append(a)
print('%.4f'%(sum(c)))

