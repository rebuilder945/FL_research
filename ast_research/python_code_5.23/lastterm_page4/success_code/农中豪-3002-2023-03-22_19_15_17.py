a=eval(input())
b=sum(a)/len(a)
if b%1==0:
    c='%.0f'%(b)
    print(c)
else:
    d='%.2f'%(b)
    print(d)
