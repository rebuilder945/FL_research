a=eval(input())
a=sum(a)/len(a)
if a%1==0:
    print(int(a))
else:
    print('%.2f'%(a))
