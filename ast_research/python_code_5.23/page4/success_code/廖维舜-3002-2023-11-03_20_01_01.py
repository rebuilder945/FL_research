a=eval(input())
x=sum(a)/int(len(a))
if sum(a)%len(a)==0:
    print('%.d'%(x))
else:
    print('%.2f'%(x))

