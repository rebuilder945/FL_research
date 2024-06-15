a=eval(input())
b=sum(a)/len(a)
if b-int(b)==0:
    print('%d'%(b))
else:
    print('%.2f'%(b))
