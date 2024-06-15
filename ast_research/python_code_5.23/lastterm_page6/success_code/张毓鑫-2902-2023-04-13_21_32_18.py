n=eval(input())
a=2
b=1
c=0
while n>0:
    c+=(a/b)
    d=b
    b=a
    a+=d
    n-=1
print('%.4f'%c)
