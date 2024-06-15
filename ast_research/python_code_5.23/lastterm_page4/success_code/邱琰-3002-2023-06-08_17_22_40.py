n=eval(input())
a=sum(n)/len(n)
if type(a)==int:
    print('%d'%(a))
else:
    print('%.2f'%(a))
