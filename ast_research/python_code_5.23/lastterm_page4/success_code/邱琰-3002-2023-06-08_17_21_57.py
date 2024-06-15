n=eval(input())
a=sum(n)/len(n)
if type(a)==int:
    print(a)
else:
    print('%.2f'%(a))
