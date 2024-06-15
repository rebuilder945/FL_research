a=eval(input())
b=sum(a)%len(a)
c=sum(a)/len(a)
if b==0:
    print('%d'%c)
else:
    print('%.2f'%c)
