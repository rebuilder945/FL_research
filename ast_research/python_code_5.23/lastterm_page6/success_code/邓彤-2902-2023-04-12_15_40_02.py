x=2
y=1
n=eval(input())
s=0
while n>0:
    s=s+x/y
    m=y
    y=x
    x+=m
    n-=1
print('%.4f'%s)
