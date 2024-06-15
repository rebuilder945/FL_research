a=eval(input())
b=sum(a)
c=len(a)
if b%c==0:
    print('%d'%(b/c))
else:
    print(f'{b/c:.2f}')
