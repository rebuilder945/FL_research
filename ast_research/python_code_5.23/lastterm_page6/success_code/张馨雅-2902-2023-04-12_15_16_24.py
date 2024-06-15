def F(num):
    up1=2
    up2=3
    next=up1+up2
    up1=up2
    up2=next
    return next
def F1(num):
    down1=1
    down2=2
    next=down1+down2
    down1=down2
    down2=next
    return next
n=eval(input())
if n==1:
    print(2.0000)
elif n==2:
    print(3.5000)
else:
    he=[3.5,]
    num=F(n)/F1(n)
    he.append(num)
    print('%.4f'%(sum(he)))
