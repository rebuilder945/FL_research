n=eval(input())
a=sum(n)/len(n)
if type(a)=='float':
    print('%.2f'%(a))
else:
    print(a)
