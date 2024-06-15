'''a=eval(input())
b=sum(a)
if b%len(a)==0:
    c=b/len(a)
    print('%d'%(c))
else:
    c=b/len(a)
    print('%.2f'%(c))'''

a=eval(input())
b=sum(a)
m=b%len(a)
if m==0:
    print(b//len(a))
else:
    print('%.2f'%(b/len(a)))
