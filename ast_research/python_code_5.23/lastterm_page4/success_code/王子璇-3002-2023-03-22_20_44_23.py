a=eval(input())
b=sum(a)
c=b/len(a)
if c%1==0:
    print("%d"%(c))
else:
    print('%.2f'%(c))
