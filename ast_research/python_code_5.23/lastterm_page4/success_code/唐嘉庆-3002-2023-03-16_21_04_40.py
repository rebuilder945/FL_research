a=eval(input())
average=sum(a)/len(a)
if average%1==0:
    print('%d'%(average))
else:
    print('%.2f'%(average))

