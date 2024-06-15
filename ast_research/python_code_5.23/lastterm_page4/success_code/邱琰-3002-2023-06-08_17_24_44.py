n=eval(input())
a=sum(n)/len(n)
if a-a//1==0:
    print(a)
else:
    print('%.2f'%(a))
