x=int(2)
y=int(1)
n=eval(input())
s=x/y
for i in range (n-1):
    m=x
    x=x+y
    y=m
    z=x/y
    s+=z
print('%.4f'%s)
