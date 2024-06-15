def F(num):
    up1=2
    up2=3
    next=1
    for i in range (3,n):
        next=up1+up2
        up1=up2
        up2=next
    return next
def F1(num):
    down1=1
    down2=2
    next=1
    for i in range (3,n):
        next=down1+down2
        down1=down2
        down2=next
    return next
n=eval(input())
if n==1:
    a=2
    print('%.4f'%a)
elif n==2:
    b=3.5
    print('%.4f'%b)
else:
    he=[3.5,]
    num=F(n)/F1(n)
    he.append(num)
    print('%.4f'%(sum(he)))
