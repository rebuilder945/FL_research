a=eval(input())
b=sum(a)
c=len(a)
d=b/c
if b%c==0:
    print('%d'%(b/c))
else:
    print('%.2f'%(d))
