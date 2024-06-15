n=eval(input())
if n==1:
    a=2/1
    print('%.4f'%a)
else:
    x1=2
    y1=1
    s=2
    for i in range(1,n):
        m=x1+y1
        n=x1
        s+=m/n
        x1=m
        y1=n
    print('%.4f'%s)

