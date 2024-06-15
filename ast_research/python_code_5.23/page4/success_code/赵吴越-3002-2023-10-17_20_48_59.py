a=eval(input())
b=sum(a)
c=len(a)
d=b/c
if b%c==0:
    print('%d'%(d))
else:
    print(f'{d:.2f}')
